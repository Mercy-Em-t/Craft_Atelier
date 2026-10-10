# UC-01: Checkout & Pay

## Data Flow Diagram (DFD)

```mermaid
flowchart LR
    %% External Entities
    C[Customer]
    MPESA[[M-Pesa STK Push API]]
    
    %% Processes
    P1([Validate Cart & Phone])
    P2([Process M-Pesa Payment])
    
    %% Data Stores
    D1[(Supabase: orders)]
    D2[(Supabase: kits inventory)]

    %% Data Flows
    C -->|Cart Items + Phone No.| P1
    P1 -->|Order Total + Phone No.| P2
    P2 -->|STK Request| MPESA
    MPESA -->|Callback Payload (Status, Amount)| P2
    P2 -->|Final Order Data| D1
    P2 -->|Deduct Stock| D2
    P2 -->|Receipt & Tracking ID| C
```

## Justification for DFD over Activity Diagram
A **Data Flow Diagram (DFD)** was chosen instead of an Activity Diagram because this use case revolves heavily around the secure exchange, transformation, and storage of sensitive transactional data across system boundaries. An Activity diagram models control flow (what happens next), but a DFD effectively maps out the complex interactions between internal processes, external data sinks (M-Pesa API), and persistent storage (Supabase PostgreSQL), which is critical for financial auditing.

## Process/Node Descriptions
- **Customer**: The external entity initiating the checkout process and providing their phone number.
- **Validate Cart & Phone ([Process])**: Validates the phone number format (e.g., 2547XX) and calculates the final subtotal.
- **Process M-Pesa Payment ([Process])**: The central process that securely requests the STK push and parses the asynchronous callback from Safaricom.
- **M-Pesa STK Push API ([[External]])**: Safaricom's external API responsible for securely authorizing and capturing the payment on the user's phone.
- **Supabase orders ([(Data Store)])**: The data sink where finalized order details and transaction statuses are persisted.
- **Supabase kits inventory ([(Data Store)])**: The data store that is updated to reflect the deduction of purchased items.
