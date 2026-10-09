# Craft Atelier - Quality Assurance (QA) & Test Plan

## Overview
This document outlines the Verification and Validation (V&V) procedures for the Craft Atelier Fulfillment Engine. It is designed to be executed during the 10-Box Pilot Run (User Acceptance Testing) to ensure the system correctly enforces financial rules and operational lifecycles.

## Verification vs. Validation
*   **Verification (Did we build it right?):** Ensuring the code behaves according to the database rules (e.g., does the DB reject a bad PIN? Do the financial snapshots trigger?).
*   **Validation (Did we build the right thing?):** Ensuring the system actually solves the business problem (e.g., does the WhatsApp message format correctly for the customer?).

---

## 🧪 E2E (End-to-End) Test Scenarios

### Test 1: Financial Snapshot & Order Creation
**Goal:** Verify that a customer can place an order and the system creates a permanent financial snapshot.
*   **Action:** Go to `storefront.html`. Add a kit to the cart. Select "Motorbike Rider (KES 300)" as delivery. Submit the M-Pesa order.
*   **Expected Result:** 
    * UI shows "Order Placed Successfully".
    * In Supabase `orders` table, the new record must have `status` = `PENDING_PAYMENT`.
    * The `subtotal_cents`, `delivery_fee_cents`, and `total_cents` columns must be explicitly populated with integers (not null).

### Test 2: Admin Financial Verification & Real-Time Sync
**Goal:** Verify that the Admin can release an order and the Warehouse UI updates instantly.
*   **Action:** 
    1. Open `admin-hub.html` on Desktop.
    2. Open `ops-packing.html` on a Tablet/Mobile device (log in as Packer).
    3. On Desktop, find the order in the Financial Verification Queue and click "Verify & Release".
*   **Expected Result:**
    * Order status changes to `QUEUED_FOR_PACKING`.
    * The Tablet UI must **automatically** update to show the new order in the queue without anyone pressing the refresh button.
    * The `order_audit_logs` table must record this transition and log the Admin's email.

### Test 3: The Unhappy Path (Reporting Stock Issues)
**Goal:** Validate that a packer can halt a fulfillment if items are missing.
*   **Action:** On the Tablet (`ops-packing.html`), click "Report Stock Issue" and type "Missing Yarn".
*   **Expected Result:**
    * The order disappears from the Packer's active queue.
    * In the database, the order status changes to `ON_HOLD` and `delivery_notes` contains "ISSUE: Missing Yarn".
    * The `order_audit_logs` table records the exception.

### Test 4: BOM Verification & Dispatch Generation
**Goal:** Verify chain of custody and OTP generation upon dispatch.
*   **Action:** Log into `ops-packing.html` as a Dispatcher. Find an order that is `STAGED_FOR_DISPATCH`. Select a Rider from the dropdown and click "Hand Off".
*   **Expected Result:**
    * Order status changes to `IN_TRANSIT`.
    * A 4-digit `delivery_pin` is securely generated and saved to the database.
    * A WhatsApp Web window opens automatically.
    * **Validation Check:** The WhatsApp message text MUST contain the Rider's name, phone number, and the newly generated 4-digit Delivery PIN.

### Test 5: Closing the Loop (Delivery PIN Validation)
**Goal:** Ensure an order cannot be completed without the customer's exact PIN.
*   **Action:** Go to `admin-hub.html` Tracking Board. Find the `IN_TRANSIT` order and click "Complete Delivery". 
    1. First, enter a fake PIN (e.g., `0000`).
    2. Then, enter the correct PIN (found in the database/WhatsApp message).
*   **Expected Result:**
    * The fake PIN must trigger a red ❌ "Invalid PIN" rejection and the order MUST remain `IN_TRANSIT`.
    * The correct PIN must succeed, change the order to `DELIVERED`, and log the final chain of custody handover in the `order_audit_logs`.
