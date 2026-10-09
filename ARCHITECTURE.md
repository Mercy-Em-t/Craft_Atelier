# Craft Atelier Fulfillment - Technical Architecture

## Overview
The platform is a web-based e-commerce and order fulfillment system for "Craft Atelier" DIY kits. It connects a storefront with an admin control hub and a live warehouse packing station. The backend leverages Supabase (PostgreSQL) for real-time state synchronization, authentication, and database management.

## Technical Stack
- **Frontend**: HTML5, CSS (vanilla/custom CSS), JavaScript (vanilla)
- **Backend / Database**: Supabase (PostgreSQL, Supabase JS Client v2)
- **Real-time Engine**: Supabase Realtime (WebSocket `postgres_changes` listener)
- **Automation Triggers**: Android SMS Forwarder

## Architecture Components

### 1. Storefront (`storefront.html`)
The customer-facing application where users browse the catalog and place orders.
- **Dynamic M-Pesa Till**: Fetches the active Paybill/Till number dynamically from the `business_settings` table.
- **Order Placement**: Captures customer details, calculates subtotal, delivery fee, and total costs before inserting a `PENDING_PAYMENT` record into the `orders` table.

### 2. Admin Hub (`admin-hub.html`)
The central command center for operators to verify payments, manage inventory, and oversee the fleet.
- **Financial Verification**: Allows admins to cross-check M-Pesa references and manually release orders to the warehouse queue (`QUEUED_FOR_PACKING`).
- **Fleet & Staff Management**: Toggle rider and staff access states.
- **Order Tracking Board**: Visualizes the entire pipeline from `PENDING_PAYMENT` to `DELIVERED`. Supports completing deliveries via a PIN check.
- **Catalog Management**: Provides UI to add/edit kits (supports JSON bulk import) and manage inventory.

### 3. Ops Packing Station (`ops-packing.html`)
A live tablet/mobile-friendly UI for warehouse staff (packers and dispatchers).
- **Real-time Queue**: Subscribes to Supabase `postgres_changes` on the `orders` table. Automatically updates the UI when an order becomes `QUEUED_FOR_PACKING` or `STAGED_FOR_DISPATCH`.
- **BOM Verification**: Packers must check off required Bill of Materials (BOM) items before sealing the box. Triggers the `verify_and_stage_order` RPC.
- **Dispatch**: Dispatchers assign an active rider, triggering the `dispatch_order` RPC, which generates a WhatsApp notification link containing the Delivery PIN.

## Critical New Additions

### 1. Order Audit Logging
Every critical state change is tracked for accountability in the `order_audit_logs` table.
- **Fields**: `order_id`, `old_status`, `new_status`, `changed_by`, `notes`.
- **Example**: Moving an order from `IN_TRANSIT` to `DELIVERED` logs the change, noting whether it was done by Admin or the Rider App, ensuring full operational traceability.

### 2. Order Financial Snapshots
The `orders` table now strictly captures the financial state at the time of checkout to prevent historical data mutation if catalog prices change:
- `subtotal_cents`: Sum of kit prices.
- `delivery_fee_cents`: Cost of the selected delivery method.
- `total_cents`: Final expected payment amount.

### 3. Delivery PIN System
To prevent theft and misdelivery:
1. **Generation**: When an order is handed to a rider (dispatched), a random 4-digit `delivery_pin` is generated and saved to the `orders` table.
2. **Distribution**: The PIN is sent to the customer via a pre-filled WhatsApp message.
3. **Verification**: The rider must collect this PIN from the customer. The Admin/Rider App checks this PIN against the database before marking the order as `DELIVERED`.

### 4. Real-Time WebSocket Synchronization
The Ops Packing UI utilizes Supabase Realtime channels to eliminate manual refreshing. When an order state changes, the UI automatically fetches the next order if it matches the current user's role (packer/dispatcher):
```javascript
client.channel('ops-orders-channel')
  .on('postgres_changes', { event: 'UPDATE', schema: 'public', table: 'orders' }, payload => {
      // Auto-fetch next order when state changes match the user's role
  }).subscribe();
```

### 5. M-Pesa Automation via PL/pgSQL
An automated M-Pesa verification flow is supported via an Android SMS Forwarder app.
- **Mechanism**: The Android app listens for M-Pesa confirmation SMS messages and forwards them to the backend database.
- **Function**: The `auto_verify_mpesa_payment` (PL/pgSQL) function is designed to be hit by this forwarder. It parses the reference code, checks the expected amount, matches it against a `PENDING_PAYMENT` order, and automatically advances its status to `QUEUED_FOR_PACKING` upon success.

### 6. Business Settings Dictionary
The `business_settings` table acts as a dynamic key-value store for global configurations, avoiding hardcoded constants in the front-end.
- **Key Example**: `mpesa_till`
- **Usage**: The Storefront and Admin Hub pull this dynamically, ensuring the business can update operational details like the Till number in real-time without redeploying the site code.
