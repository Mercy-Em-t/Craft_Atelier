# UC-12: Manage Global Inventory

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    Admin -->|JSON Stock Count| P1([Calculate Diff])
    DB_In[(Current DB Stock)] -->|Current Values| P1
    P1 -->|Delta Updates| DB_Out[(Supabase: inventory)]
    P1 -->|Audit Log| Log[(Supabase: audit_logs)]
```
## Justification
A **Data Flow Diagram** is required for inventory reconciliation because it involves pulling existing state, computing a differential (delta), and updating the single source of truth.
## Process Descriptions
- **Calculate Diff**: The system compares the physical count uploaded by the Admin against the digital count to find shrinkage.
