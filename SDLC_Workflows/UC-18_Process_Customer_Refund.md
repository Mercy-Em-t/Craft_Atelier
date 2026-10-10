# UC-18: Process Customer Refund

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    Support -->|Refund Amount| P1([Initiate Refund])
    P1 -->|B2C Payload| MPESA[[M-Pesa B2C API]]
    MPESA -->|Success Callback| P2([Update Ledgers])
    P2 -->|Deduct Royalty| DB1[(creator_payouts)]
    P2 -->|Mark Refunded| DB2[(orders)]
```
## Justification
A **Data Flow Diagram** is critical here because refunding money alters multiple ledgers (deducting from the company AND deducting from the Creator's future payout).
## Process Descriptions
- **Initiate Refund**: Triggers the outbound money transfer to the customer.
- **Update Ledgers**: Ensures the Creator is not paid a royalty for a refunded item.
