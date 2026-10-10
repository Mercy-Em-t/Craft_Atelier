# Elicitation Techniques & Innovative Use Cases Report

This document details the creative elicitation process used to generate new, innovative features for the Craft Atelier project. The final selected use cases were strictly evaluated for **orthogonality**—meaning they introduce entirely new dimensions of functionality (e.g., content creation, accessibility, reverse logistics) rather than simply upgrading existing e-commerce features.

---

## I. Elicitation Techniques Used

To break away from standard e-commerce features (like shopping carts and payment gateways), the following four creativity-based elicitation techniques were employed:

1. **Relaxation of Constraints:** We temporarily removed assumed limitations. For example, we relaxed the constraint that "users must use their hands to scroll through instructions" and the constraint that "learning is a one-way visual street."
2. **Analogical Reasoning:** We mapped successful paradigms from completely different industries onto crafting. We asked: *"What if Craft Atelier behaved like Strava (fitness), Duolingo (language), or TikTok (social)?"*
3. **Systemic Thinking:** We analyzed the macro-ecosystem beyond the initial sale, looking at the lifecycle of the yarn (waste management) and the emotional state of the user during the crafting process.
4. **Brainstorming:** A rapid, unconstrained "blue-sky" ideation phase where no idea was deemed too expensive or impossible, allowing us to generate raw concepts that were later refined.

---

## II. Comprehensive List of Generated Ideas (Names & Short Descriptions)

*The following 30 ideas were generated during Phase 1 (Divergent Thinking).*

1. **Voice-Controlled Pattern Reader:** Hands-free navigation using voice commands ("Next row").
2. **Left-Handed Mirror Engine:** A toggle that physically mirrors all tutorial videos and swaps left/right text.
3. **The "Panic Button":** A button triggering a 5-minute SOS live video call with a craft expert.
4. **AR "Try Before You Buy":** Augmented reality preview of the finished bag on your table.
5. **"Gift a Mistake" Rescue Service:** Mail us your tangled mess; we fix it and mail it back.
6. **Boda Boda "First Stitch" Concierge:** Delivery riders trained to stay 5 minutes to help you tie the first knot.
7. **Virtual Crafting Lounge:** VR integration for remote group crafting.
8. **Strava for Crafters:** Local leaderboards for crafting speed and consistency.
9. **Duolingo for Crafts:** Gamified XP, streaks, and unlockable rewards for daily crafting.
10. **Tinder for Crafts:** Matchmaking logic to find local craft buddies.
11. **HelloFresh "Leftover Recipes":** An algorithm that generates micro-patterns based on your exact leftover yarn scraps.
12. **TikTok Auto-Timelapse Builder:** Background camera capture that stitches a hyper-lapse of your crafting session.
13. **Spotify-Style "Wrapped":** End-of-year data visualization of stitches made and screen-free hours logged.
14. **Circular Economy "Scrap Return":** Reverse logistics allowing users to hand scrap yarn back to riders for recycling credits.
15. **IoT Warehouse Weight Sensors:** Smart bins that auto-order yarn from wholesalers.
16. **Dynamic Off-Peak Pricing:** Automated price drops during slow warehouse hours.
17. **Creator "Modular" SKU Engine:** Drag-and-drop web builder for creators to instantly generate new warehouse BOMs.
18. **B2B Real-Time Team Dashboard:** Live progress bars for HR managers tracking their employees' kits.
19. **B2B "Sabotage" Mode:** Gamified corporate mode where departments send "knot challenges" to rivals.
20. **AI Color-Palette Matcher:** Image recognition that maps an uploaded outfit photo to yarn colors.
21. **Smart Crochet Hooks:** Bluetooth hardware that automatically counts stitches.
22. **Blind Box Subscriptions:** Mystery kits where the final product is a surprise.
23. **AI-Generated Encouragement:** Automated SMS check-ins sounding like a supportive grandmother.
24. **Braille / Audio-Descriptive Patterns:** Deep accessibility mode for visually impaired users.
25. **Micro-Investing API:** Finishing a kit triggers a KES 500 bank deposit to your savings.
26. **Blockchain Authenticity:** NFTs verifying the bag was made using an official creator pattern.
27. **Gamified Unboxing:** QR codes on box flaps unlocking secret digital patterns.
28. **"Rent-a-Tool" Library:** Boda boda delivery and retrieval of expensive ergonomic hooks.
29. **Live Twitch-style CALs:** Embedded live "Crochet-A-Long" streams.
30. **Yarn "Tasting" Menu:** A low-cost sample envelope of 20 luxury yarns.

---

## III. Highest Value Orthogonal Use Cases (Phase 2 Selection)

*After evaluating the 30 ideas against technical feasibility and business value, we selected the following 5 new use cases. They are strictly **orthogonal** to our existing e-commerce checkout and warehouse dispatch use cases, introducing entirely new functional dimensions.*

### 1. UC-INNOV-01: Automated Timelapse Generator (Social/Marketing Dimension)
* **Description:** A web-app feature that accesses the user's mobile camera via HTML5. The user props their phone against the box, and the system captures a frame every 10 seconds, automatically stitching it into a high-speed timelapse video ready for TikTok/Instagram.
* **Value Proposition:** Orthogonal to buying/selling. It transforms the physical crafting process into an automated user-generated content (UGC) marketing engine, directly solving the Gen-Z persona's desire for social validation.

### 2. UC-INNOV-02: Left-Handed Mirror Engine (Accessibility Dimension)
* **Description:** A UI toggle that applies CSS transformation (`transform: scaleX(-1)`) to all HTML5 video players and dynamically swaps the words "Left" and "Right" in the text pattern arrays.
* **Value Proposition:** Orthogonal to standard video playback. It algorithmically solves a massive accessibility hurdle, instantly capturing the 10% of the market (left-handed users) who traditionally abandon crafting tutorials.

### 3. UC-INNOV-03: Voice-Controlled Pattern Navigation (Hands-Free UX Dimension)
* **Description:** Integration of the Web Speech API into the storefront. Users can verbally command the tutorial to "Go to Next Row" or "Repeat Video" without dropping their hook and yarn.
* **Value Proposition:** Orthogonal to traditional touch-screen navigation. It directly addresses the physical friction of crafting (hands being occupied), ensuring beginners don't lose their place and abandon the project.

### 4. UC-INNOV-04: On-Demand "Panic Button" (Synchronous Support Dimension)
* **Description:** A WebRTC video-call widget embedded in the pattern page. If a beginner drops a stitch, they press the button to initiate a 5-minute live video consultation with a craft expert in the Ops Hub.
* **Value Proposition:** Orthogonal to static text/video tutorials. It introduces live, synchronous human intervention at the exact moment of highest user frustration, drastically reducing refund requests and project abandonment.

### 5. UC-INNOV-05: Circular Economy Scrap Return (Reverse Logistics Dimension)
* **Description:** A feature allowing users to request a "Scrap Pickup" on their dashboard. Our Boda Boda riders, who normally return empty-handed from deliveries, pick up the leftover yarn scraps, crediting the user's account with KES 200.
* **Value Proposition:** Orthogonal to outbound delivery. It introduces a reverse logistics pipeline that solves ESG (environmental) requirements for our Corporate B2B buyers while reducing our own COGS (Cost of Goods Sold) by recycling the stuffing.
