# 📦 Standard Operating Procedure: Warehouse & Admin Hub

## 🎯 Overview
This Standard Operating Procedure (SOP) outlines the updated workflows for the Fulfillment Station and Admin Headquarters. All systems are now synchronized via real-time databases, minimizing manual refreshes and ensuring strict chain-of-custody through Delivery PIN verification.

---

## 1️⃣ Fulfillment Station (Ops Packing)

### Real-Time Order Queue
- **No Manual Refreshes Needed:** The packing station tablets are now equipped with real-time syncing. Whenever an order is released by finance, it will automatically appear in your queue. The "CONNECTING..." badge will change to show active queue counts dynamically.

### BOM Packing Verification
1. Review the Customer Card and Order requirements on your screen.
2. Carefully pack the items, checking off each required component on the screen (e.g., Curated Yarn Bundles, Ergonomic Hook, Notions Pack, etc.).
3. **Verify All Items & Seal Box:** Once all checkboxes (including the Bonus Charm) are ticked, click this button to stage the order for dispatch. 

### Exception Handling: Report Stock Issue
- If you realize a required component is missing or damaged, **DO NOT** verify the order.
- Click the red **"Report Stock Issue"** button.
- This will immediately set the order status to `ON_HOLD` and remove it from your active packing queue, alerting management to rectify the inventory problem.

---

## 2️⃣ Dispatch & Rider Hand-off

### Assigning a Carrier
1. Once an order is `STAGED_FOR_DISPATCH`, it will move to the Handover view.
2. Click **"Assign Carrier / Hand Off"**.
3. Select the active motorbike rider from the dropdown menu and confirm dispatch.

### WhatsApp Notification & Delivery PIN
- Upon hand-off, the system generates a secure **4-digit Delivery PIN**.
- A WhatsApp Click-to-Chat window will automatically open on your device.
- **Action Required:** Send the pre-filled message to the customer. It contains the rider's contact details and their unique Delivery PIN, which they must provide upon arrival.

---

## 3️⃣ Tracking & Delivery Confirmation (Admin Hub)

### Order Tracking Board
- The Admin Hub features a live tracking board filterable by status (`QUEUED_FOR_PACKING`, `PACKING_IN_PROGRESS`, `STAGED_FOR_DISPATCH`, `IN_TRANSIT`, `DELIVERED`).
- Admins can monitor real-time fulfillment progression across the warehouse.

### Completing a Delivery (PIN Required)
- Once the rider reaches the customer, they must ask the customer for their 4-digit Delivery PIN.
- On the Admin Hub (or via Rider App), click **"Complete Delivery"** on an `IN_TRANSIT` order.
- **Mandatory Step:** You **MUST** enter the exact 4-digit Delivery PIN. 
  - *If the PIN is correct:* The order is marked `DELIVERED` and logged in the audit trail.
  - *If the PIN is incorrect:* The system will reject the status change. You must confirm the correct PIN with the customer.

---

## 4️⃣ Catalog & Inventory Management

### Adding New Products
Admins can manage the product catalog directly from the Admin Hub's Catalog & Inventory section. When clicking **"+ Add New Kit"**, you will be prompted to choose between two methods:

1. **Single Kit (Option '1'):** Add a kit manually by typing in the Title, Price (in KES), and Initial Inventory Count one by one.
2. **Bulk Import via JSON (Option '2'):** Instantly add multiple products by pasting a JSON array of kits. 
   - *Example format:* `[{"title": "Beginner Kit", "price_cents": 250000, "inventory_count": 15}, {"title": "Advanced Kit", "price_cents": 450000, "inventory_count": 5}]`
   - This is highly recommended for seasonal catalog updates or initial data population.

### Editing Existing Products
- Click **"Edit"** next to any kit to update its inventory count or price. The system will safely archive the old record and create a new version to maintain strict financial and inventory history.
