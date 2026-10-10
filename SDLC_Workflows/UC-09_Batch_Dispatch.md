# UC-09: Batch Dispatch & Delivery PIN

## Activity Diagram

```mermaid
stateDiagram-v2
    [*] --> ReviewPackedOrders: Dispatcher
    ReviewPackedOrders --> SelectCheckboxes: Dispatcher
    SelectCheckboxes --> AssignRider: Dispatcher selects Boda Rider
    
    AssignRider --> GeneratePIN: System creates 4-digit PIN
    GeneratePIN --> NotifyCustomer: System sends WhatsApp API Message
    NotifyCustomer --> HandoffToRider: Dispatcher physically gives boxes to Rider
    
    HandoffToRider --> Transit: Rider drives to Customer
    Transit --> RequestPIN: Rider asks Customer for PIN
    
    RequestPIN --> DispatcherValidation: Dispatcher types PIN into Hub
    DispatcherValidation --> InvalidPIN: PIN is incorrect
    InvalidPIN --> RequestPIN: Rider asks again
    
    DispatcherValidation --> ValidPIN: PIN is correct
    ValidPIN --> MarkDelivered: Order permanently locked to DELIVERED
    MarkDelivered --> [*]
```

## Justification: Activity Diagram vs. Data Flow Diagram
An **Activity Diagram** is the optimal choice for UC-09 because it involves complex chronological handoffs between multiple human actors (the Dispatcher, the System, the Boda Rider, and the Customer). While a DFD would only show the data passing between these entities, an Activity Diagram effectively models the operational workflow, illustrating exactly *who* is responsible for *what* step and the sequence of those physical responsibilities (like refusing to hand over the box until the PIN is verified).

## Process Descriptions
- **ReviewPackedOrders**: The Dispatcher evaluates orders that are taped shut and ready for delivery.
- **SelectCheckboxes**: The Dispatcher logically groups multiple orders based on neighborhood routes.
- **AssignRider**: The Dispatcher assigns the batch to a specific Boda Rider from a dropdown list.
- **GeneratePIN**: The system creates the secure chain-of-custody token.
- **NotifyCustomer**: The system automatically sends a WhatsApp alert to the Customer so they know the rider is en route.
- **HandoffToRider**: The physical collection of the batch from the warehouse.
- **RequestPIN / DispatcherValidation**: The loop where the Boda rider calls the Dispatcher to verify the customer's PIN before releasing the physical goods.
