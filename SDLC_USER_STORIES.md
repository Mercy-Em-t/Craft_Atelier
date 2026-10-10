# Craft Atelier: Deep-Dive Agile User Stories (Phased Approach)

*This document expands the core Use Cases into highly granular User Stories. Each Use Case is broken down chronologically into distinct Phases (e.g., Pre-condition, Execution, Edge-Cases, Post-condition) to capture the exact software flow.*

---

## Part 1: Core E-Commerce & Intake

### UC-01: Checkout & Pay
**Phase 1: Cart & Validation**
* **US-1.1:** As a *Customer*, I want to see my order subtotal, delivery fee, and grand total clearly separated before checkout, so that there are no hidden surprises.
* **US-1.2:** As a *Customer*, I want the system to validate my Kenyan phone number format (e.g., 07XX or 2547XX) in real-time before I click Pay, so that the M-Pesa prompt doesn't fail.
* **US-1.3:** As a *Gifter*, I want to specify a separate "Delivery Phone Number", so that my friend receives the tracking SMS instead of me.

**Phase 2: Execution & Waiting**
* **US-1.4:** As a *Customer*, I want to receive an instant M-Pesa STK push prompt on my phone, so that I don't have to navigate away to my SIM toolkit.
* **US-1.5:** As a *Customer*, I want to see a "Waiting for Payment confirmation" spinner on the website, so that I know the system is listening for my PIN entry.

**Phase 3: Callbacks & Edge Cases**
* **US-1.6:** As a *System Admin*, I want the backend to strictly verify the M-Pesa callback payload (checking the actual amount paid vs expected amount), so that users can't exploit the API by paying KES 1 for a KES 2500 kit.
* **US-1.7:** As a *Customer*, if my M-Pesa times out or I have insufficient funds, I want to see a clear error message and a "Retry Payment" button, so that I don't have to re-enter all my address details.


### UC-02: Bulk Address CSV Upload
**Phase 1: Upload & Parsing**
* **US-2.1:** As an *HR Manager*, I want to download a blank CSV template, so that I know exactly how to format my 50 employee addresses.
* **US-2.2:** As an *HR Manager*, I want to upload the filled CSV and have the system instantly parse it, displaying a preview of the 50 orders on my screen before I pay.

**Phase 2: Error Handling**
* **US-2.3:** As an *HR Manager*, if row 14 of my CSV has a missing phone number, I want the system to highlight that specific row in red, so that I can fix it without re-uploading the entire document.

**Phase 3: Execution**
* **US-2.4:** As a *Dispatcher*, I want a bulk corporate order to automatically split into 50 individual tracking IDs in the Operations Hub, so that I can route them to different Boda riders.


### UC-03: Create Modular SKU
**Phase 1: The Visual Builder**
* **US-3.1:** As an *Independent Creator*, I want to drag-and-drop existing yarn colors and hardware into a web form, so that I can design my custom kit visually.
* **US-3.2:** As an *Independent Creator*, I want the system to automatically calculate the Cost of Goods Sold (COGS) based on my selections, so that I know the baseline price.

**Phase 2: Financials & Publishing**
* **US-3.3:** As an *Independent Creator*, I want to set my desired royalty margin (e.g., 15%), so that the system automatically calculates the final retail price for my audience.
* **US-3.4:** As a *System Admin*, I want the Creator's submission to automatically generate a valid Bill of Materials (BOM) in the Supabase `kits` table, so that the Warehouse Packers can start fulfilling it immediately without my manual intervention.

---

## Part 2: Innovation & Engagement

### UC-04: View Interactive Tutorial
**Phase 1: Onboarding**
* **US-4.1:** As a *Beginner*, I want a welcome screen explaining how to hold the hook and yarn, so that I have the basic posture right before starting Row 1.

**Phase 2: Playback & Navigation**
* **US-4.2:** As a *Beginner*, I want the video to auto-loop the specific stitch I am on, so that I can watch it 5 times without taking my hands off my crochet hook.
* **US-4.3:** As a *Beginner*, I want clear "Previous Row" and "Next Row" buttons, so that I can easily navigate the pattern visually.
* **US-4.4:** As a *Craft-Curious Beginner*, I want to use voice commands to say "Next Step", so that I don't have to touch my sticky phone screen.

**Phase 3: State Management**
* **US-4.5:** As a *Returning Beginner*, I want the app to remember exactly which row I was on when I closed my browser yesterday, so that I don't have to scroll to find my place.


### UC-06: Toggle Left-Handed Mirror
**Phase 1: Activation**
* **US-6.1:** As a *Left-Handed Crafter*, I want a single, highly visible toggle switch at the top of the tutorial, so that I can activate left-handed mode instantly.

**Phase 2: System Response**
* **US-6.2:** As a *Left-Handed Crafter*, I want the UI to physically mirror the HTML5 video player via CSS, so that I can mimic the instructor's hand movements exactly.
* **US-6.3:** As a *Left-Handed Crafter*, I want the text instructions to dynamically swap "left" and "right" when the mirror mode is active, so that I don't have to do mental gymnastics while reading.


---

## Part 3: Warehouse Operations

### UC-07: Scan & Verify BOM (Bill of Materials)
**Phase 1: Selection**
* **US-7.1:** As a *Warehouse Packer*, I want to see a Kanban column of all 'Pending' orders on my tablet, so that I can tap the one at the top of the queue to begin packing.

**Phase 2: Execution (Checklist)**
* **US-7.2:** As a *Warehouse Packer*, I want to see a digital checklist of every physical item (yarn, hooks, needles) required for this specific SKU, so that I don't forget anything.
* **US-7.3:** As a *Warehouse Packer*, I want to physically tap each item on the screen as I place it in the box, turning the row green, so that I track my progress.

**Phase 3: Completion**
* **US-7.4:** As a *Warehouse Packer*, I want the tablet screen to flash a large "SUCCESS" prompt when all items are verified, automatically moving the order to the 'Packed' column, so that I can rapidly tape the box shut and move to the next order.


### UC-09: Batch Dispatch Orders
**Phase 1: Batch Selection**
* **US-9.1:** As a *Dispatcher*, I want to see a Kanban column of all 'Packed' orders awaiting a rider, categorized by neighborhood (e.g., Kilimani, Westlands), so that I know the geographic backlog.
* **US-9.2:** As a *Dispatcher*, I want to use multi-select checkboxes to highlight 5 orders going to the same area, so that I can batch them together.

**Phase 2: Rider Assignment**
* **US-9.3:** As a *Dispatcher*, I want to select a specific Boda Rider from a dropdown list to attach them to the batched orders, logging their name and plate number for accountability.

**Phase 3: System Triggers**
* **US-9.4:** As a *System Admin*, I want the system to automatically generate a secure 4-digit Delivery PIN for each order the moment they are dispatched, initiating the chain of custody.
* **US-9.5:** As a *Customer*, I want to receive an automated WhatsApp message containing my Delivery PIN and the Rider's phone number exactly when my box leaves the warehouse, so that I can prepare to receive it.


### UC-10: Input Delivery PIN
**Phase 1: The Handoff**
* **US-10.1:** As a *Boda Boda Rider*, I want the customer to give me their secret PIN upon arrival, so that I can prove I handed the box to the correct person.

**Phase 2: Verification**
* **US-10.2:** As a *Dispatcher*, I want to type the PIN provided by the rider into the Operations Hub, so that the system can verify it against the database.
* **US-10.3:** As a *Dispatcher*, if the PIN is incorrect, I want the system to flash a red error and refuse to close the order, so that packages cannot be stolen or misdelivered.

**Phase 3: Post-Condition**
* **US-10.4:** As a *System Admin*, I want the order status to permanently lock to `DELIVERED` once the correct PIN is entered, concluding the order lifecycle.

---

## Part 4: Admin Governance & Royalties

### UC-13: View Financial & Audit Logs
**Phase 1: Transparency**
* **US-13.1:** As a *System Admin*, I want to click on any order and see an immutable timeline of who changed its status (e.g., "Packed by John at 10:04 AM", "Dispatched by Mary at 11:15 AM"), so that I can investigate bottlenecks.

**Phase 2: Financial Integrity**
* **US-13.2:** As a *System Admin*, I want the financial snapshot (subtotal, fees, tax) to save permanently as a snapshot row on the `orders` table upon checkout, so that past accounting records aren't ruined if I increase the price of a kit table tomorrow.


### UC-16: Disburse Creator Royalties
**Phase 1: Calculation**
* **US-16.1:** As a *System Admin*, I want the dashboard to automatically sum all cleared royalties owed to a specific creator for the month, so that I don't have to calculate it manually in Excel.

**Phase 2: Execution**
* **US-16.2:** As a *System Admin*, I want to click a single "Disburse Funds" button to trigger an M-Pesa B2C API transfer to the creator's registered phone number.

**Phase 3: Notification & Reconciliation**
* **US-16.3:** As an *Independent Creator*, I want to receive an automated SMS receipt the moment the Admin triggers my payout, so that I know the funds have hit my M-Pesa account.
* **US-16.4:** As a *System Admin*, I want the Creator's dashboard to automatically reset their "Pending Balance" to zero once the M-Pesa callback confirms the transfer was successful, maintaining accurate ledgers.

---

## Part 5: The Missing 8 Core Workflows (Deep-Dive)

### UC-05: Trigger Panic Button SOS
**Phase 1: Execution**
* **US-5.1:** As a *Frustrated Beginner*, I want a persistent red "SOS" button visible at all times during the video tutorial, so that I can get help instantly without searching for a contact page.
* **US-5.2:** As a *System Admin*, I want the video to pause automatically the moment the SOS button is pressed, so that the user doesn't lose their place in the pattern.

**Phase 2: Routing & Resolution**
* **US-5.3:** As a *Dispatcher*, I want my dashboard to ring loudly and flash red when an SOS is triggered, so that I can answer the WebRTC call immediately.


### UC-08: Flag Stock Exception
**Phase 1: Identification**
* **US-8.1:** As a *Warehouse Packer*, I want a "Flag Issue" button next to every item on my digital checklist, so that I can report if a skein of yarn is damaged or missing from the bin.

**Phase 2: System Routing**
* **US-8.2:** As a *System Admin*, I want an order with a flagged exception to automatically change its status to `ON_HOLD`, so that it is physically prevented from reaching the Dispatch queue.
* **US-8.3:** As an *Inventory Manager*, I want a real-time dashboard of all active stock exceptions, so that I can walk to the warehouse floor and replace the damaged items.


### UC-11: Update Business Settings
**Phase 1: Configuration**
* **US-11.1:** As a *System Admin*, I want to type a new M-Pesa Till Number into a secure settings form, so that I can change payment routing dynamically without deploying new code.
* **US-11.2:** As a *System Admin*, I want the system to reject any Till Number that isn't exactly 6 or 7 digits, so that I don't accidentally break the storefront checkout flow.

**Phase 2: Cache Invalidation**
* **US-11.3:** As a *Customer*, I want the Storefront cache to invalidate immediately when the Admin changes the Till Number, so that I never send money to an outdated account.


### UC-12: Manage Global Inventory
**Phase 1: Execution**
* **US-12.1:** As an *Inventory Manager*, I want to upload a CSV of my physical warehouse count, so that the system can automatically compare it against the digital database.

**Phase 2: Reconciliation**
* **US-12.2:** As an *Inventory Manager*, I want the system to highlight any negative deltas (shrinkage) in red, so that I can immediately investigate missing or stolen stock.


### UC-14: Generate Tax Compliance CSV
**Phase 1: Execution**
* **US-14.1:** As a *Corporate Accountant*, I want to select a strict start and end date for my tax export, so that I only pull financial data for the current calendar month.

**Phase 2: System Formatting**
* **US-14.2:** As a *Corporate Accountant*, I want the exported CSV headers to strictly match the KRA e-TIMS API schema, so that I don't have to spend hours manually formatting Excel columns before submitting my taxes.


### UC-15: View Royalty Dashboard
**Phase 1: Visualization**
* **US-15.1:** As an *Independent Creator*, I want to see a line chart of my sales over the last 30 days, so that I can track the success of my recent social media marketing campaigns.

**Phase 2: Privacy Enforcement**
* **US-15.2:** As a *System Admin*, I want the database Row Level Security (RLS) to explicitly hide the names and phone numbers of the customers from the Creator's dashboard, so that we comply with Kenya Data Privacy laws.


### UC-17: Review Support Escalations
**Phase 1: Context Gathering**
* **US-17.1:** As a *Support Agent*, I want to click on a ticket and instantly see the exact Delivery PIN and the Packer's name associated with that order, so that I can investigate claims of "missing items".

**Phase 2: Resolution**
* **US-17.2:** As a *Support Agent*, I want to tag a ticket as either "Resolved" or "Refund Requested", so that my manager can review my triage decisions before money is sent.


### UC-18: Process Customer Refund
**Phase 1: Execution**
* **US-18.1:** As a *Support Agent*, I want to specify a partial refund amount (e.g., KES 500), so that I can compensate a customer for a late delivery without refunding the entire KES 2,500 order.

**Phase 2: Ledger Math**
* **US-18.2:** As a *System Admin*, I want the refunded amount to automatically deduct from the Creator's next royalty payout, so that the company doesn't lose money paying royalties on canceled transactions.
