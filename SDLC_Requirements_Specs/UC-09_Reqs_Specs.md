# UC-09: Batch Dispatch Orders

**Kano Priority:** 9. One-Dimensional

---

## Requirement 1
> **The Dispatcher physically hands a grouped batch of packages to a designated Boda Rider.**

### System Specifications
1. The System shall allow the Dispatcher to select multiple 'PACKED' orders via UI checkboxes.
2. The System shall assign a selected `rider_id` to the batch.
3. The System shall randomly generate a 4-digit `delivery_pin` for each order.
4. The System shall trigger the WhatsApp API to send the PIN to the respective customers.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The physical transfer of cardboard boxes from the warehouse dock to the motorcycle.
- **Interface Phenomenon (The Machine):** The API call transmitting the 4-digit PIN string to the WhatsApp Business server.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Dispatcher actually hands the boxes to the rider they selected in the UI.
- **A2:** The Customer's phone number is registered on WhatsApp.
