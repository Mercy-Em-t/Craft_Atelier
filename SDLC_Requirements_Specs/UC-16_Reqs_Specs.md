# UC-16: Disburse Creator Royalties

**Kano Priority:** 6. Must-Be

---

## Requirement 1
> **The Admin legally transfers fiat currency to the Independent Creators for their monthly sales.**

### System Specifications
1. The System shall sum all orders where `status = DELIVERED` and `royalty_paid = FALSE`.
2. The System shall construct a JSON payload formatted to the M-Pesa B2C API specification.
3. The System shall transmit the payload and await the asynchronous callback.
4. The System shall update `royalty_paid = TRUE` only upon receiving a successful callback.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The deposit of Kenyan Shillings into the Creator's personal M-Pesa account.
- **Interface Phenomenon (The Machine):** The secure HTTPS POST request traversing the network to Safaricom.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The Creator's registered phone number is capable of receiving funds (not blocked or over limits).
- **A2:** The company has correctly calculated the 15% margin.
