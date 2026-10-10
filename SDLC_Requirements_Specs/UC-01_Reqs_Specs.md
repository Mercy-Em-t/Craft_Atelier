# UC-01: Checkout & Pay

**Kano Priority:** 8. One-Dimensional

---

## Requirement 1
> **The Customer successfully pays for their physical craft kit using their mobile phone.**

### System Specifications
1. The System shall validate the user's phone input against Kenyan regex standards (e.g., ^2547).
2. The System shall initiate an STK Push by communicating with the Daraja API.
3. The System shall parse the Daraja Callback to verify the `Amount` paid matches the `Subtotal`.
4. The System shall insert a new row into the `orders` table upon successful validation.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The customer entering their secret M-Pesa PIN into their physical SIM Toolkit.
- **Interface Phenomenon (The Machine):** The Daraja API webhook POSTing a JSON success payload to the Supabase Edge Function.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The customer's mobile device is powered on and has cellular reception.
- **A2:** Safaricom's Daraja API is not experiencing an outage.
