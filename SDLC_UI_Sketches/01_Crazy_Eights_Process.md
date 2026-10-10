# UI Design: Crazy Eights Process & Iteration Review

As part of our UI/UX ideation phase, our team employed the **Crazy Eights** methodology for the 4 major screens of the platform. The team spent 8 minutes generating 8 rough sketches per screen, conducted design critiques, and iterated on the best concepts.

## 1. Storefront Checkout Screen (Mobile)
### Round 1 Review
* **Positives (Keep):** Large, thumb-friendly 'Pay' buttons at the absolute bottom of the screen; explicit separation of Cart Total vs. Delivery Fee.
* **Negatives (Discard):** Hiding the phone number input behind an accordion (adds unnecessary clicks); using small dropdowns for country codes (prone to fat-finger errors).
### Round 2 Focus
Refined the sketch to feature a persistent, always-visible M-Pesa phone number field with inline validation, ensuring the user is never more than 1 tap away from the STK push.

## 2. Interactive Tutorial & SOS (Mobile)
### Round 1 Review
* **Positives (Keep):** The floating action button (FAB) for the SOS Panic Button; placing the video player at the absolute top of the viewport.
* **Negatives (Discard):** Burying the "Left-Handed Mirror" toggle in a separate settings menu (users won't find it); cluttering the screen with too much text instruction.
### Round 2 Focus
Moved the Left-Handed Mirror toggle directly beneath the video player for instant access. Stripped away heavy text paragraphs in favor of massive 'Next Row / Prev Row' navigation arrows.

## 3. Ops Packing Checklist (Tablet)
### Round 1 Review
* **Positives (Keep):** Massive checkboxes for easy tapping; color-coding items (e.g., Red yarn vs Blue yarn) for visual scanning.
* **Negatives (Discard):** Swiping gestures to flag exceptions (warehouse workers wearing gloves struggled with swiping in tests).
### Round 2 Focus
Replaced swipe gestures with a dedicated, hard-to-miss 'Flag Exception' button next to every item. Added a clear 'Order Complete' success flash.

## 4. Admin Royalty Dashboard (Desktop)
### Round 1 Review
* **Positives (Keep):** The visual line chart showing 30-day sales velocity; grouping unpaid payouts in a unified table.
* **Negatives (Discard):** Making Admins click into individual creator profiles to pay them (too slow for scale).
### Round 2 Focus
Added a global "Batch Disburse All" button above the table, allowing the Admin to clear all pending M-Pesa B2C payments with a single click.
