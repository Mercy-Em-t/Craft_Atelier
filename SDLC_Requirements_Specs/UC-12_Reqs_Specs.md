# UC-12: Manage Global Inventory

**Kano Priority:** 5. Must-Be

---

## Requirement 1
> **The Inventory Manager reconciles the digital inventory count with the physical warehouse stock.**

### System Specifications
1. The System shall accept a CSV file containing SKU IDs and integer counts.
2. The System shall compute the delta (difference) between the uploaded integer and the existing `stock_count` in the database.
3. The System shall update the database with the new integers and log the delta in the `audit_logs` table.
4. The System shall render a table highlighting any negative deltas in red CSS.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The physical counting of boxes on warehouse shelves.
- **Interface Phenomenon (The Machine):** The parsing of the uploaded CSV file stream into memory.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Inventory Manager performed the manual count accurately.
- **A2:** No orders are actively being fulfilled (modifying stock) during the CSV upload window.
