# UC-11: Update Business Settings

**Kano Priority:** 18. Indifferent

---

## Requirement 1
> **The Admin changes the M-Pesa routing Till number without modifying source code.**

### System Specifications
1. The System shall provide an authenticated form to update the `business_settings` table.
2. The System shall validate the string length of the inputted Till number.
3. The System shall issue a cache invalidation command to edge nodes.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The business opening a new corporate bank account with Safaricom.
- **Interface Phenomenon (The Machine):** The invalidation of cached API responses on the CDN.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The new Till number is fully activated by Safaricom before the Admin inputs it.
