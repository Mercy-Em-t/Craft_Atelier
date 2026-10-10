# UC-10: Input Delivery PIN

**Kano Priority:** 2. Must-Be

---

## Requirement 1
> **The Boda Boda Rider only hands the physical package to the correct verified Customer.**

### System Specifications
1. The System shall expose a numerical input field on the Dispatcher dashboard.
2. The System shall query the `orders` table to match the inputted PIN against the generated `delivery_pin` column.
3. The System shall transition the order state to DELIVERED only if the string match is strictly identical.
4. The System shall log the Dispatcher's user ID timestamping the verification event.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The physical verbal exchange of a 4-digit code between the Customer and Rider.
- **Interface Phenomenon (The Machine):** The keyboard input events registered on the Dispatcher's web browser interface.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Customer has not shared their PIN with a malicious third party.
- **A2:** The Dispatcher enters the exact numbers dictated over the phone without typos.
