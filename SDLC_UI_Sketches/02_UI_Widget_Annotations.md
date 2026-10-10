# UI Widget Annotations & Specifications

Below are the detailed annotations for the GUI widgets on our 4 primary screens, categorizing them strictly by Input (control/trigger) and Output (presentation).

---

## Screen 1: Storefront Checkout (Mobile)
* **Output Widget [Cart Summary Text]:** 
  * *Description:* Presents the final calculated fiat amount, itemized by subtotal, tax, and delivery fee.
* **Input Widget [Phone Number Field]:** 
  * *Interaction:* User taps and types their 9-digit Safaricom number. 
  * *System Response:* Triggers real-time regex validation; borders turn red if invalid.
* **Input Widget [M-Pesa Pay Button]:** 
  * *Interaction:* User taps the primary call-to-action button. 
  * *System Response:* Disables the button to prevent double-clicks, triggers the Safaricom Daraja API STK Push, and loads a waiting spinner.

---

## Screen 2: Interactive Tutorial (Mobile)
* **Output Widget [Video Player]:** 
  * *Description:* Presents the looping MP4 video of the current crochet stitch.
* **Input Widget [Left-Handed Toggle]:** 
  * *Interaction:* User taps the switch. 
  * *System Response:* Injects a CSS `transform: scaleX(-1)` to the video container, flipping it horizontally.
* **Input Widget [Panic SOS Button]:** 
  * *Interaction:* User taps the floating red button. 
  * *System Response:* Pauses the video player and initiates a WebRTC connection request to the Admin Operations Hub.
* **Input Widget [Next/Prev Navigation Arrows]:** 
  * *Interaction:* User taps the arrows. 
  * *System Response:* Updates the video timestamp variables to loop the next/previous set of instructions.

---

## Screen 3: Ops Packing Checklist (Tablet)
* **Output Widget [BOM List]:** 
  * *Description:* Presents the exact physical items (Yarn colors, hook sizes) required for the active order.
* **Input Widget [Item Checkbox]:** 
  * *Interaction:* Packer taps the row. 
  * *System Response:* UI flashes green, marks item as verified. If all items are verified, triggers a DB status update to `PACKED`.
* **Input Widget [Flag Exception Button]:** 
  * *Interaction:* Packer taps the warning icon next to a damaged item. 
  * *System Response:* Triggers a modal asking for the exception reason (Damaged/Missing) and updates order status to `ON_HOLD`.

---

## Screen 4: Admin Royalty Dashboard (Desktop)
* **Output Widget [Sales Line Chart]:** 
  * *Description:* Presents a visual graph of total sales volume over the last 30 days, pulled from the `order_audit_logs`.
* **Output Widget [Pending Payouts Table]:** 
  * *Description:* Presents a list of Creators, their accumulated unpaid royalties, and their registered M-Pesa phone numbers.
* **Input Widget [Disburse Royalties Button]:** 
  * *Interaction:* Admin clicks the primary button above the table. 
  * *System Response:* Triggers a batch POST request to the M-Pesa B2C API for all rows in the table, deducting funds from the corporate bank account.
