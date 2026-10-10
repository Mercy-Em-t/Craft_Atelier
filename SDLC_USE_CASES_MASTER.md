# Craft Atelier: Master Use Case Document (Functional Groupings)
This document contains all 60 Use Cases grouped strictly by their Functional System Modules (Epics), outlining the complete architectural blueprint for the software.

## 1. Storefront & E-Commerce Module (B2C)
*Handling the core customer buying journey, checkout, and personalization.*
1. Customer browses available DIY kits by category (Bags, Hats, Accessories).
2. Customer pays via M-Pesa and receives immediate visual confirmation.
3. Customer provides delivery details using an interactive GPS Map Pin.
4. Customer applies a promotional discount code (e.g., "CROCHET20") at checkout.
5. Customer abandons their cart and the system sends a gentle WhatsApp reminder 2 hours later.
6. Customer buys a kit as a "Gift" and includes a custom printed note.
7. Customer takes a "Skill Level Quiz" and the system recommends the perfect beginner kit.
8. AI analyzes past purchases to suggest the most likely next project for returning customers.
9. Customer uses a "Custom Kit Builder" to mix-and-match specific yarn colors before checkout.
10. Customer uses an Augmented Reality (AR) mobile app to project a 3D model of the bag on their table.

## 2. B2B, Wholesale & Subscriptions Module
*Handling recurring revenue and bulk/corporate orders.*
11. Corporate HR orders 50 branded kits for an event and generates an official PDF Quote.
12. Boutique shops log into a hidden "Wholesale Tier" to buy kits at a 30% discount.
13. System reserves B2C inventory so a sudden B2B bulk order doesn't wipe out the public website.
14. Customer signs up for a "Kit of the Month" subscription billed automatically via M-Pesa.
15. Customer clicks a button to "Pause" or "Skip" their subscription box for a specific month.

## 3. Warehouse Operations & WMS Module
*Handling physical packing, Bill of Materials, and performance.*
16. Packer views a real-time Kanban board of all queued orders.
17. Packer verifies the exact Bill of Materials (BOM) checklist before sealing a box.
18. Packer flags an order as "On Hold" due to missing stock (e.g., out of Navy Blue yarn).
19. Packer prints a physical shipping label/packing slip to tape to the outside of the box.
20. Admin resolves "On Hold" warehouse exceptions and re-queues them.
21. Admin views a dashboard tracking "Packer Efficiency" (boxes packed per hour).
22. Admin sets up a pop-up shop at a weekend market and uses a POS tablet view to ring up walk-ins.
23. System instantly deducts pop-up shop sales from central warehouse inventory to prevent double-selling.

## 4. Inventory & Supply Chain Module
*Handling cataloging, supplier orders, and stock integrity.*
24. Admin dynamically adds new kits or bulk imports them via JSON.
25. Admin conducts a "Monthly Stocktake" to reconcile physical yarn with the database.
26. System automatically alerts the Admin when a specific yarn drops below 10 units.
27. Admin generates a digital Purchase Order (PO) to send to the yarn manufacturer.
28. Warehouse logs the "Batch/Lot Number" of incoming yarn for quality control tracking.
29. Admin views a "Predictive Forecast" showing which kits will run out of stock next month.

## 5. Logistics & Fleet Management Module
*Handling routing, rider dispatch, and nationwide shipping.*
30. Dispatcher groups multiple orders together for batch processing.
31. Dispatcher securely hands off boxes to riders and system generates a 4-digit Delivery PIN.
32. System sends the customer a WhatsApp message containing their secure PIN.
33. Admin/Dispatcher marks the order as "Delivered" only after verifying the customer's PIN.
34. Customer is not home, so rider marks delivery as "Failed/Attempted" to automatically reschedule.
35. Rider gets a flat tire and digitally transfers their batched orders to another rider's app.
36. Admin calculates weekly payouts for Boda Boda riders based on successful deliveries.
37. Customer selects "Pick Up In-Store" at checkout and chooses a specific 2-hour collection slot.
38. System integrates with a national courier API (e.g., G4S) for deliveries outside Nairobi.
39. System tracks the carbon footprint of delivery routing to optimize eco-friendly dispatch.

## 6. Financial & Administrative Control Module
*Handling revenue, taxes, refunds, and security.*
40. Admin updates the global M-Pesa Till Number without touching code.
41. Admin cancels impossible orders and logs the exact refund reason for auditing.
42. System protects against duplicate M-Pesa transaction codes at the database level.
43. System automatically generates a PDF receipt and emails it to the customer upon payment.
44. Admin exports a compliant CSV report of all VAT collected for the Kenya Revenue Authority (KRA).
45. System blocks a user's IP address if they spam fake M-Pesa codes 5 times.
46. Staff member clicks a secure "Forgot Password" link to reset their Ops Hub access.

## 7. Community, Creator & Support Module
*Handling user loyalty, external creators, and post-purchase support.*
47. Customer uploads a photo of their finished creation to the Storefront to leave a review.
48. Customer refers a friend and earns loyalty points toward their next kit.
49. Customer initiates a digital return/exchange request for receiving the wrong color.
50. Customer opens a live WhatsApp support ticket with a crafting expert if they get stuck.
51. Local designers submit their own crochet patterns to be sold as kits (Revenue Share model).
52. Admin automatically calculates and pays out monthly royalties to pattern designers.
53. Instagram influencer generates a unique affiliate link to earn commissions on sales.
54. System triggers an automated email to previous "Bag Kit" buyers when a "Wallet Kit" launches.
55. Customer unlocks a digital "Master Crafter" profile badge after finishing 5 kits.
56. Customers vote on prototype designs to decide which kit Craft Atelier manufactures next.
57. Customer returns excess/unused yarn for store credit (Zero Waste initiative).
58. Customer downloads the Craft Atelier app for push notifications of step-by-step videos.
59. Marketing views a Nairobi Heat Map showing which neighborhoods buy the most kits.
60. System calculates "Customer Lifetime Value" (CLV) to identify top VIP crafters.


## Module 8: Innovative Engagement & Accessibility (Phase 2)
*These use cases were elicited using advanced creativity techniques to provide strictly orthogonal value beyond standard e-commerce features.*

**UC-061: Left-Handed Mirror Engine**
* **Actor:** Storefront Customer (Left-handed)
* **Goal:** To watch tutorial videos and read patterns formatted specifically for left-handed crafting.
* **Flow:** User clicks the "Left-Handed Mode" toggle. The system applies a CSS mirror transformation to all HTML5 video players and dynamically swaps the strings "Left" and "Right" in the text instructions.

**UC-062: Auto-Timelapse Builder**
* **Actor:** Storefront Customer (Social Media User)
* **Goal:** To easily generate a hyper-lapse video of their crafting process for social media.
* **Flow:** User grants HTML5 camera permissions in the tutorial UI. The system silently captures a frame every 10 seconds. Upon completion, the system stitches the frames into a downloadable MP4 video optimized for TikTok/Instagram.

**UC-063: The "Panic Button" (Craft Paramedic)**
* **Actor:** Storefront Customer (Beginner)
* **Goal:** To get immediate human help when a stitch is dropped or a mistake is made.
* **Flow:** User clicks the red "Panic Button" on the tutorial page. The system opens a WebRTC/WhatsApp video link routing directly to an on-call crafting expert in the Ops Hub for a 5-minute intervention.

**UC-064: AI "Roast My Project" Gamification**
* **Actor:** Storefront Customer (Failed Project)
* **Goal:** To find humor in a failed project and receive a discount to try again.
* **Flow:** User uploads a photo of their tangled/failed project. The system sends the image to an AI Vision API (prompted with a comedic persona), returns a customized "roast", and generates a 20% discount promo code for a new kit.

**UC-065: Creator Modular SKU Builder**
* **Actor:** Independent Designer (Creator)
* **Goal:** To independently build and launch a physical kit without manual Admin intervention.
* **Flow:** Creator logs into the Creator Portal. They drag-and-drop pre-existing inventory items (e.g., Red Yarn, Wooden Handles) into a visual builder. The system automatically calculates the COGS, adds the creator's 15% royalty, and inserts a new SKU into the Supabase `kits` table.
