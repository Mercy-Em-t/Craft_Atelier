# UC-10: Input Delivery PIN

## Activity Diagram
```mermaid
stateDiagram-v2
    [*] --> ArriveAtCustomer: Boda Rider
    ArriveAtCustomer --> RequestPIN: Rider asks Customer
    RequestPIN --> CallDispatcher: Rider reads PIN over phone
    CallDispatcher --> TypePIN: Dispatcher enters PIN
    TypePIN --> ValidatePIN: System
    ValidatePIN --> Invalid: Incorrect PIN
    Invalid --> RequestPIN
    ValidatePIN --> Valid: Correct PIN
    Valid --> MarkDelivered: Status locked
    MarkDelivered --> [*]
```
## Justification
An **Activity Diagram** is necessary because it relies on a multi-actor chronological verification loop that refuses to proceed until a strict condition (valid PIN) is met.
## Process Descriptions
- **RequestPIN**: The physical handoff blocker.
- **ValidatePIN**: The backend check ensuring the provided PIN matches the `delivery_pin` column in Supabase.
