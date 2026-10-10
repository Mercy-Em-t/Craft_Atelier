# Craft Club / DIY Kit Platform Requirements

## Phase 1: Minimum Viable Product (The "Must-Haves")
This phase focuses on a lean, 10-Box Pilot Run to validate demand and unit economics with minimal engineering debt.

### Core Product
* **1 Flagship Kit**: A beginner-friendly product (e.g., ribbed shoulder bag or tote) available in limited colorways.
* **Pre-started Pieces**: 10 base foundation pieces pre-crocheted to eliminate beginner frustration (zero-frustration engineering).
* **Curated Components**: Zero-fray tube yarn, ergonomic hook, darning needle, and safety locking stitch markers.
* **Unboxing Experience**: Branded E-flute corrugated mailer boxes (250x180x70mm) and a surprise maker charm tucked inside.
* **Instructional Material**: A physical 6-panel printed accordion card with a QR code linking to a 90-second silent top-down video guide.

### Sales & Operations (Day-1 Lean Setup)
* **Storefront**: A single clean landing page or Instagram Reel/Story with a direct WhatsApp order button.
* **Communications Pipe**: Standard WhatsApp Business app on a shared phone with 3 pre-saved Quick Replies (`/order`, `/rider`, `/checkin`).
* **Fulfillment Station**: Printed paper checklists stuck to the packing table; manual ticking of BOM before taping the box.
* **Backend Tracking**: Google Sheet or Notion board for active tracking (Name, Phone, Delivery Landmark, Status).
* **Logistics**: Manual booking of local riders (e.g., motorbikes) and manual texting of dispatch updates.

---

## Phase 2: Scaling and Automation (The "Nice-to-Haves")
This phase introduces software automation, strict access controls, and scaled catalog options after the pilot run succeeds.

### Core Product
* **Expanded Catalog**: Progressively add more variations, eventually scaling to 40 SKUs (spanning a clear difficulty/lifestyle ladder: Tier 1 Gateway, Tier 2 Flagship, Tier 3 Premium).

### Sales & Operations (Automated Setup)
* **Storefront Integration**: Custom dynamic web app connected to a live database.
* **Backend System**: Full Supabase integration (`kits`, `orders`, and `fulfillment_logs` tables) with custom Row-Level Security (RLS) and audit trail RPCs.
* **Payment Ingestion**: Automated M-Pesa Daraja STK Push or Card payment webhook to trigger `QUEUED_FOR_PACKING` immediately upon payment.
* **Fulfillment Station**: Mobile web app with digital lockout checkboxes (Staff cannot dispatch without full BOM verification).
* **Communications**: WhatsApp Cloud API webhook listeners & bot replies (Two-way automated messaging).
  * Automated alerts triggered by state changes (`QUEUED_FOR_PACKING`, `STAGED_FOR_DISPATCH`, `IN_TRANSIT`).
  * Automated Webhook Verification for delivery notes (automatically appending customer replies to delivery records).
* **Role-Based Access Control (RBAC)**:
  * **Operations Staff Dashboard**: Event buttons only, hidden financials, restricted to specific operational state transitions.
  * **Business Admin Dashboard**: Full revenue analytics, margin oversight, override capabilities, inventory management.


### Phase 2: Innovation & Viral Engagement (The "Orthogonal" Features)
* **REQ-INV-01 [Accessibility]:** The storefront MUST support a global "Left-Handed Mode" that visually mirrors video content and dynamically swaps directional text.
* **REQ-INV-02 [Marketing]:** The system SHOULD include an HTML5 background camera capture utility to stitch crafting timelapses.
* **REQ-INV-03 [Support]:** The tutorial interface MUST include a "Panic Button" routing to a synchronous video call with Ops.
* **REQ-INV-04 [Retention]:** The system SHOULD utilize an AI Vision API to analyze failed project photos, generate comedic feedback, and issue retention discount codes.
* **REQ-INV-05 [B2B Scaling]:** The Creator Portal MUST feature a visual drag-and-drop SKU builder that automatically writes new kit configurations (BOMs) to the Supabase database.
