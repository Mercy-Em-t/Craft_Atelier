# UC-17: Review Support Escalations

## Activity Diagram
```mermaid
stateDiagram-v2
    [*] --> OpenTicket: Support Agent
    OpenTicket --> ReadHistory
    ReadHistory --> ResolveIssue
    ResolveIssue --> NeedsRefund: Yes
    NeedsRefund --> UC18: Trigger Refund Flow
    ResolveIssue --> CloseTicket: No Refund Needed
    CloseTicket --> [*]
```
## Justification
An **Activity Diagram** accurately models the triage branching logic of a support desk (escalating to refunds vs. standard closures).
## Process Descriptions
- **ReadHistory**: Loading the customer's previous order and chat history.
- **Trigger Refund Flow**: A logical handoff to the financial system (UC-18).
