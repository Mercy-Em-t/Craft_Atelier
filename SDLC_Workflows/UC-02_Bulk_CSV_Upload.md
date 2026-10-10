# UC-02: Bulk Address CSV Upload

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    HR[HR Manager] -->|CSV File| P1([Parse & Validate CSV])
    P1 -->|Validation Errors| HR
    P1 -->|Valid Batch| P2([Process Bulk M-Pesa])
    P2 -->|STK Push| MPESA[[M-Pesa API]]
    MPESA -->|Payment Success| P3([Split into Orders])
    P3 -->|Individual Rows| DB[(Supabase: orders)]
```
## Justification
A **Data Flow Diagram (DFD)** is used because this is a heavy data-transformation task (converting a single CSV into 50 distinct database rows and triggering a bulk payment API).
## Process Descriptions
- **Parse & Validate CSV**: Ensures phone numbers and addresses meet schema requirements.
- **Process Bulk M-Pesa**: Requests a single large payment from the HR Manager.
- **Split into Orders**: Transforms the batch array into distinct delivery tracking IDs in the DB.
