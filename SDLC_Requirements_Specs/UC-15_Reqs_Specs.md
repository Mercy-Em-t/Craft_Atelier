# UC-15: View Royalty Dashboard

**Kano Priority:** 10. One-Dimensional

---

## Requirement 1
> **The Creator monitors their financial success without viewing private customer data.**

### System Specifications
1. The System shall enforce Row Level Security (RLS) ensuring `creator_id` matches the JWT token.
2. The System shall aggregate sales data over time and pass it to a charting library.
3. The System shall explicitly exclude `customer_phone` and `customer_address` from the JSON response.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The Creator's psychological understanding of their marketing performance.
- **Interface Phenomenon (The Machine):** The filtering of data packets prior to transmission over the network.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Creator keeps their authentication credentials secure.
- **A2:** The charting library renders the aggregated data accurately.
