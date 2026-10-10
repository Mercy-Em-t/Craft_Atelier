# UC-16: Disburse Creator Royalties

## Data Flow Diagram (DFD)

```mermaid
flowchart TD
    %% External Entities
    Admin[System Admin]
    MPESA[[M-Pesa B2C API]]
    SMS[[WhatsApp / SMS Gateway]]

    %% Processes
    Calc([Sum Cleared Royalties])
    Init([Initiate M-Pesa Disbursement])
    Recon([Reconcile Payout Ledger])

    %% Data Stores
    AuditDB[(Supabase: order_audit_logs)]
    PayoutDB[(Supabase: creator_payouts)]

    %% Data Flows
    Admin -->|Click Disburse| Calc
    AuditDB -->|Cleared Sales Data| Calc
    Calc -->|Total owed per creator| Init
    Init -->|B2C Payment Instructions| MPESA
    MPESA -->|Callback (Success/Fail)| Recon
    Recon -->|Update Ledger to 'Paid'| PayoutDB
    Recon -->|Payment Receipt| SMS
```

## Justification for DFD over Activity Diagram
A **Data Flow Diagram** was chosen over an Activity Diagram because this use case is fundamentally a data-driven integration process moving money across systems. Disbursing royalties relies on querying financial logs, talking to banking APIs (M-Pesa B2C), and writing to immutable ledgers via asynchronous callbacks. A DFD clearly illustrates the lineage and security of this financial information, which is critical for auditing and tax compliance.

## Process/Node Descriptions
- **System Admin**: The user triggering the global payout cron/script.
- **Sum Cleared Royalties ([Process])**: Reads raw metrics from the audit logs and calculates owed royalties (excluding refunds).
- **Initiate M-Pesa Disbursement ([Process])**: Retrieves pending payouts and transmits payment instructions to the M-Pesa B2C API.
- **Reconcile Payout Ledger ([Process])**: Processes asynchronous callbacks from M-Pesa to confirm transaction statuses and update financial records.
- **M-Pesa B2C API ([[External]])**: The external financial service executing money movement out of the company bank account.
- **WhatsApp / SMS Gateway ([[External]])**: The service that notifies the Creator that their money has arrived.
- **Supabase order_audit_logs ([(Data Store)])**: Repository for incoming monetizable events (sales).
- **Supabase creator_payouts ([(Data Store)])**: The system of record for completed financial payouts.
