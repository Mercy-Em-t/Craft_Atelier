# UC-11: Update Business Settings

## Data Flow Diagram (DFD)
```mermaid
flowchart LR
    Admin -->|New M-Pesa Till No.| P1([Validate Input])
    P1 -->|Validated Config| DB[(Supabase: business_settings)]
    DB -->|Invalidate Cache| P2([Storefront Client])
```
## Justification
A **Data Flow Diagram** captures how configuration data is pushed to a central store and propagated to active edge clients (cache invalidation).
## Process Descriptions
- **Validate Input**: Ensures the Till number is exactly 6 or 7 digits.
- **Invalidate Cache**: Forces the storefront to fetch the new Till number immediately to prevent payment routing errors.
