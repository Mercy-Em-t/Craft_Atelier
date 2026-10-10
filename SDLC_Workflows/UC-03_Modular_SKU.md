# UC-03: Create Modular SKU

## Data Flow Diagram (DFD)

```mermaid
flowchart LR
    %% External Entities
    Creator[Independent Creator]
    
    %% Processes
    P1([Assemble Modular Components])
    P2([Calculate Financial Margins])
    
    %% Data Stores
    D1[(Supabase: raw_materials)]
    D2[(Supabase: kits)]

    %% Data Flows
    Creator -->|Select Yarn, Hook, Pattern| P1
    D1 -->|Component COGS| P1
    P1 -->|Assembled BOM| P2
    Creator -->|15% Royalty Margin| P2
    P2 -->|Final Retail Price| P2
    P2 -->|New Kit Config| D2
    D2 -->|SKU Success Confirmation| Creator
```

## Justification for DFD over Activity Diagram
A **Data Flow Diagram** was chosen over an Activity Diagram because managing modular SKUs is fundamentally an aggregation of data from various sources to assemble a final composite product. While an Activity Diagram shows *how* the user clicks through the web page, a DFD clearly shows *where* the dependencies lie, mapping out the flow of data from the raw materials database, through the pricing engine, and finally resting in the main kits catalog database.

## Process/Node Descriptions
- **Independent Creator**: The user providing the configuration data for the new kit.
- **Assemble Modular Components ([Process])**: Ingests configuration data and fetches component costs from the raw materials database.
- **Calculate Financial Margins ([Process])**: Computes the dynamic final retail price based on the selected modules (COGS) plus the Creator's royalty percentage.
- **Supabase raw_materials ([(Data Store)])**: The source database containing individual physical parts and their wholesale costs.
- **Supabase kits ([(Data Store)])**: The sink database where the newly assembled modular SKU (the BOM) is stored for customers to buy.
