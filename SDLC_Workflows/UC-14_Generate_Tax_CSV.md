# UC-14: Generate Tax Compliance CSV

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    Admin -->|Click Export| P1([Extract Sales Data])
    DB[(orders & royalties)] -->|Raw Data| P1
    P1 -->|Transform to e-TIMS Format| P2([Generate CSV])
    P2 -->|CSV Download| Admin
    P2 -->|Optional: API Push| KRA[[KRA e-TIMS API]]
```
## Justification
A **Data Flow Diagram** models the exact ETL (Extract, Transform, Load) pipeline required for legal tax compliance formatting.
## Process Descriptions
- **Transform to e-TIMS Format**: Maps our internal database columns (e.g., `subtotal_cents`) to the exact header requirements mandated by the Kenya Revenue Authority.
