# UC-15: View Royalty Dashboard

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    Creator -->|Auth Token| P1([Filter by Creator_ID])
    DB[(Supabase: orders)] -->|Sales Data| P1
    P1 -->|Sum Royalties| P2([Calculate Pending Balance])
    P2 -->|Render Dashboard| Creator
```
## Justification
A **Data Flow Diagram** ensures that data leakage does not occur, explicitly showing the filter layer that prevents Creator A from seeing Creator B's sales data.
## Process Descriptions
- **Filter by Creator_ID**: A Row Level Security (RLS) enforcement step ensuring data privacy.
- **Calculate Pending Balance**: Sums all un-disbursed orders.
