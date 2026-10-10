# Elicitation of Innovative Requirements

This document uses advanced creativity techniques to generate out-of-the-box features for the Craft Atelier platform. 

---

## Phase 1: Idea Generation (Divergent Thinking)
*Using four creative elicitation techniques, we generated 30 wild, unconstrained use cases.*

### Technique 1: Relaxation of Constraints
*What if we break the physical laws of our business model (e.g., "Shipping takes time," "Hands must hold the yarn")?*
1. **Voice-Controlled Pattern Reader:** "Alexa/Siri, next row." (Hands-free crafting).
2. **Left-Handed Mirror Engine:** A single toggle that automatically flips all videos, UI, and text patterns for left-handed crafters.
3. **The "Panic Button":** A button in the UI that instantly initiates a 5-minute SOS video call with an expert to fix a dropped stitch.
4. **AR "Try Before You Buy":** Use your phone camera to see the finished crochet bag sitting on your actual living room table before buying the kit.
5. **"Gift a Mistake" Rescue Service:** Customers mail a hopelessly tangled/ruined project to the warehouse; our experts fix it and mail it back.
6. **Boda Boda "First Stitch" Concierge:** The delivery rider is trained to sit with you for 3 minutes and help you tie the first slipknot before leaving.
7. **Virtual Crafting Lounge:** Crochet in your living room while wearing a VR headset (Meta Quest) alongside 5 other strangers in a virtual cafe.

### Technique 2: Analogical Reasoning
*If Craft Atelier was [X successful app]...*
8. **Strava for Crafters:** Local leaderboards. "You are the 4th fastest person in Nairobi to finish the Chunky Tote Bag!"
9. **Duolingo for Crafts:** Gamified learning. Earn XP, maintain a 7-day crafting streak, and unlock secret yarn colors.
10. **Tinder for Crafts:** Swipe to find a local "Craft Buddy" to meet up with at a coffee shop.
11. **HelloFresh "Leftover Recipes":** Input your leftover yarn scraps into the app, and it generates a micro-pattern (e.g., a keychain) so zero yarn is wasted.
12. **TikTok Auto-Timelapse Builder:** Prop your phone against the box. The app auto-records, edits, speeds up, and adds trending music to a timelapse of you making the bag, ready to post.
13. **Spotify-Style "Wrapped":** An end-of-year dashboard showing "You crocheted 5,000 stitches and spent 40 hours screen-free this year!"

### Technique 3: Systemic Thinking
*Looking at the entire supply chain and ecosystem from a macro level.*
14. **Circular Economy "Scrap Return":** Customers put scrap yarn back in the box and give it to the Boda rider on their next order for a KES 200 discount. We recycle it into stuffing.
15. **IoT Warehouse Weight Sensors:** Smart bins that automatically trigger a WhatsApp message to the local wholesaler when black yarn drops below 5kg.
16. **Dynamic Off-Peak Pricing:** The Supabase engine automatically drops kit prices by 15% at 2:00 PM on Tuesdays to keep warehouse packers busy during slow hours.
17. **Creator "Modular" SKU Engine:** A web interface where Creators drag-and-drop handles, colors, and bag bodies. It instantly generates a new BOM (Bill of Materials) for the warehouse without our CEO doing any manual data entry.
18. **B2B Real-Time Team Dashboard:** HR Managers log in and see a live progress bar of which employees have finished their corporate wellness kits.
19. **B2B "Sabotage" Mode:** Departments compete. Marketing can send a "Knot Challenge" to Accounting to slow down their crafting progress.

### Technique 4: Brainstorming (Pure Blue-Sky)
*No bad ideas, just pure generation.*
20. **AI Color-Palette Matcher:** Upload a photo of your favorite outfit, and the AI custom-builds a yarn color kit to match it perfectly.
21. **Smart Crochet Hooks (Hardware):** A Bluetooth crochet hook with a gyroscope that counts your stitches automatically on your phone.
22. **Blind Box / Mystery Subscriptions:** You don't know what you are making until you finish row 10.
23. **AI-Generated Encouragement:** The app texts you in the voice of a supportive grandmother if it notices you haven't opened the pattern in 3 days.
24. **Braille / Audio-Descriptive Patterns:** Highly accessible UI for visually impaired crafters.
25. **Micro-Investing API:** Every time you finish a kit, the app automatically deposits KES 500 from your bank into a savings account (rewarding good habits).
26. **Blockchain Authenticity:** An NFT proving your bag is an *official* design by Creator Chloe, not a knock-off.
27. **Gamified Unboxing:** QR codes hidden inside the cardboard flaps that unlock secret digital patterns.
28. **"Rent-a-Tool" Library:** Don't buy the KES 5,000 ergonomic hook; rent it for the week and give it back to the Boda rider.
29. **Live Twitch-style CALs:** "Crochet-A-Long" streams integrated directly into the storefront.
30. **Yarn "Tasting" Menu:** A KES 500 envelope containing 1-meter samples of 20 luxury yarns just to feel the textures before buying a big kit.

---

## Phase 2: Evaluation & Selection (Convergent Thinking)
*We evaluated the 30 ideas against our Lean Canvas, Personas, and technical feasibility. We discarded hardware (Smart Hooks), gimmicks (NFTs), and regulatory nightmares (Micro-investing). We whittled it down to the **7 Most Promising Innovative Use Cases**.*

### 1. Voice-Controlled Pattern Navigation (The "Hands-Free" Mode)
* **Value Prop:** Beginners have their hands full of yarn and hooks. Tapping a phone screen to scroll to the next step causes them to drop their work.
* **Implementation:** A simple Web Speech API integration in the Storefront that listens for "Next Step" or "Repeat that."

### 2. The Auto-Timelapse Builder (For "Pinterest Patty")
* **Value Prop:** Gen-Z users craft for social validation. By building a feature that auto-records and speeds up their crafting session into a TikTok-ready video, we turn every customer into a viral marketing engine.
* **Implementation:** Access the mobile device camera via HTML5, capture frames every 10 seconds, and stitch them via a lightweight cloud function.

### 3. Left-Handed Mirror Engine (Accessibility Win)
* **Value Prop:** 10% of the world is left-handed, and crafting tutorials are notoriously hostile to them. This instantly captures an underserved, highly loyal market.
* **Implementation:** A single UI toggle that applies `transform: scaleX(-1)` to all tutorial videos and swaps words like "Left/Right" in the text pattern.

### 4. The "Panic Button" (Craft Paramedic)
* **Value Prop:** Solves the absolute highest point of friction for Beginners (dropping a stitch and not knowing how to fix it). They will pay a premium subscription for this safety net.
* **Implementation:** WebRTC video call integration in the Storefront that rings an on-call expert in the Ops Hub.

### 5. Circular Economy "Scrap Return"
* **Value Prop:** Lowers our Cost of Goods Sold (COGS) by recycling stuffing material, and appeals heavily to corporate ESG (Environmental, Social, Governance) goals for B2B HR buyers.
* **Implementation:** Add a "Request Scrap Pickup" button in the B2B portal that routes a Boda rider during their empty return trips.

### 6. Creator "Modular" SKU Engine
* **Value Prop:** Creators want to sell kits, but our Admin bottleneck is manually creating new SKUs in the database. This lets Creators self-serve and instantly launch products.
* **Implementation:** A drag-and-drop web builder for Creators that auto-generates a Bill of Materials (BOM) in Supabase.

### 7. AI Color-Palette Matcher
* **Value Prop:** Mass personalization without increasing warehouse complexity (since we already stock the primary colors).
* **Implementation:** A simple vision API that extracts hex codes from an uploaded photo and maps them to the closest yarn colors in our Supabase inventory.
