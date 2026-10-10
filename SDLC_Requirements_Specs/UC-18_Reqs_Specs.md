# UC-18: Process Customer Refund

**Kano Priority:** 1. Must-Be

---

## Requirement 1
> **The Support Agent ensures the customer's bank account receives the correct refunded monetary value.**

### System Specifications
1. The System shall provide a secure input field restricted to authorized Support roles for entering a refund amount.
2. The System shall transmit an HTTP POST payload to the M-Pesa B2C API containing the customer's phone number and refund amount.
3. The System shall await a synchronous 200 OK response and an asynchronous JSON callback confirming transaction success.
4. The System shall automatically deduct the refunded amount from the associated Creator's pending royalty ledger.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The physical transfer of fiat currency into the Customer's M-Pesa wallet.
- **Interface Phenomenon (The Machine):** The M-Pesa B2C API webhook callback payload received by the System's server.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The M-Pesa B2C API is operational and the company's working capital account has sufficient balance.
- **A2:** The Support Agent is acting in good faith and not committing fraud.
