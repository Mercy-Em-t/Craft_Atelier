# End-to-End System Architecture

This document details the target state (Phase 2) automated infrastructure for the DIY Kit fulfillment pipeline.

## 1. High-Level Fulfillment Pipeline

The architecture is built around a state-driven fulfillment pipeline that decouples Customer Communication from Physical Operations:

1. **Order Ingest & Inventory Lock**: The storefront captures checkout details and decrements component batch counts. Status: `QUEUED_FOR_PACKING`.
2. **Automated Welcome & Note Intake**: Webhooks fire to WhatsApp Cloud API to confirm the order and request any delivery notes (e.g., gate codes).
3. **Fulfillment Verification**: Packing operator uses a mobile web app to check off physical BOM components. Status transitions to `PACKING_IN_PROGRESS` and then `STAGED_FOR_DISPATCH`.
4. **Dispatch Routing**: Order assigned to a carrier (e.g., Doorstep Motorbike Rider, Pickup Station). Status updates to `IN_TRANSIT` triggering WhatsApp tracking alerts via Edge Functions.
5. **Post-Delivery Care**: A delayed job/webhook checks in with the customer 24 hours later to ensure successful onboarding.

## 2. Core Data Models (Supabase / PostgreSQL)

The system relies on three core relational tables:

*   **`kits` (Catalog)**: Stores `id`, `title`, `slug`, `price_cents`, `inventory_count`, and a JSONB `bom_items` array detailing exactly what goes into each kit.
*   **`orders` (Metadata & State)**: Tracks `id`, `order_number`, customer details, `delivery_type`, and the crucial `status` enum (`QUEUED_FOR_PACKING`, `PACKING_IN_PROGRESS`, `STAGED_FOR_DISPATCH`, `IN_TRANSIT`, `DELIVERED`, `CANCELLED`).
*   **`fulfillment_logs` (Audit)**: The "Zero-Mistake" check log. Records `order_id`, `packed_by`, `checked_items`, `bonus_item_included`, `carrier_name`, and timestamp events for staging and dispatch.

## 3. Role-Based Dashboards & State Machine

Strict Role-Based Access Control (RBAC) paired with a PostgreSQL Finite State Machine (FSM) prevents human error.

### Operations Staff Dashboard
*   **Access**: Mobile-optimized standalone HTML (Progressive Web App) talking directly to Supabase REST via CDN.
*   **Capabilities**: Can only advance specific RPC actions (`verify_and_stage_order`, `dispatch_order`).
*   **Visibility**: Financials and margins are strictly hidden. Views only recipient name, delivery landmark, phone number, and BOM checklists.
*   **Enforcement**: Physical Lockout (Verify button disabled until all checkboxes are clicked). Zero verification bypasses (RPC writes directly to audit logs).

### Business Admin Dashboard
*   **Capabilities**: Full override capabilities, refund triggers, address editing, inventory management, and catalog updates.
*   **Visibility**: Gross margins, inventory replenishment alerts, fulfillment logs, revenue analytics, and BOM margins.

## 4. Automations & Integrations

*   **Database Webhooks**: Listen for row updates on the `orders` table. When an order transitions to `IN_TRANSIT`, it fires a trigger to a Supabase Edge Function.
*   **Supabase Edge Functions**: Receives the webhook payload, extracts carrier info from `fulfillment_logs`, and POSTs a formatted message to the WhatsApp Business Cloud API.
*   **Two-Way Messaging**: Customer replies on WhatsApp hit a Meta Webhook which invokes a backend Edge Function to append their notes directly to the `orders.delivery_notes` column on the packing screen.

## 5. Suggested Complementary Systems

To ensure the system performs even better, consider integrating the following complementary systems:

1. **Inventory & Supplier Management System (ERP Lite)**: To automate wholesale aggregation, tracking raw material levels (yarn cones, hardware) and alerting when safety stock drops below thresholds, automatically drafting supplier purchase orders.
2. **Customer Relationship Management (CRM) & Marketing Automation**: Since the model relies heavily on the "Thanks, I made it" social currency, integrating a CRM (like Klaviyo or HubSpot) to track UGC (User Generated Content) and trigger referral reward flows could boost organic acquisition.
3. **Automated Label Printing**: Integrating a thermal printer API (e.g., PrintNode) into the `STAGED_FOR_DISPATCH` transition to instantly print shipping waybills and QR codes, eliminating handwritten rider notes and avoiding manual transcription errors.
4. **Interactive Video Platform for Troubleshooting**: A system like VideoAsk integrated into the Post-Delivery Care loop to let customers send short video clips of their tangled yarn and get asynchronous video replies from the crafting team.
