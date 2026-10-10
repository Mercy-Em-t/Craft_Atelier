# UC-08: Flag Stock Exception

**Kano Priority:** 4. Must-Be

---

## Requirement 1
> **The Packer stops processing an order if a physical item is damaged, and alerts the Inventory Manager.**

### System Specifications
1. The System shall provide an 'Exception' button on the BOM packing interface.
2. The System shall present a dropdown menu of exception reasons (e.g., 'Damaged', 'Missing').
3. The System shall update the order status to `ON_HOLD` in the PostgreSQL database.
4. The System shall emit a real-time notification event to the Admin dashboard.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The visual identification of frayed or wet yarn by human eyes.
- **Interface Phenomenon (The Machine):** The database UPDATE command changing the status enum to ON_HOLD.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Packer correctly identifies damage according to QA standards.
- **A2:** The Admin is actively monitoring the dashboard to see the real-time notification.
