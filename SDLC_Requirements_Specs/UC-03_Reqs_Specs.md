# UC-03: Create Modular SKU

**Kano Priority:** 14. Attractive

---

## Requirement 1
> **The Creator assembles a new product utilizing existing warehouse materials.**

### System Specifications
1. The System shall render a drag-and-drop interface containing components from the `raw_materials` table.
2. The System shall dynamically calculate the COGS (Cost of Goods Sold) as components are added.
3. The System shall calculate the final retail price by adding the Creator's 15% royalty margin to the COGS.
4. The System shall insert the finalized JSON structure into the `kits` database.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The Creator designing a logical curriculum or pattern for their audience.
- **Interface Phenomenon (The Machine):** The dynamic JavaScript arithmetic executing in the Creator's browser.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The `raw_materials` database accurately reflects the physical costs incurred by the business.
- **A2:** The Creator provides a valid PDF pattern to accompany the physical materials.
