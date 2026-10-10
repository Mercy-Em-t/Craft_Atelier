# UC-06: Toggle Left-Handed Mirror

## Activity Diagram
```mermaid
stateDiagram-v2
    [*] --> StandardMode
    StandardMode --> ClickToggle: User clicks "Left-Handed"
    ClickToggle --> ApplyCSSMirror: System scales video X(-1)
    ApplyCSSMirror --> SwapText: System swaps "Left/Right" strings
    SwapText --> LeftHandedMode
    LeftHandedMode --> ClickToggle: User clicks standard
    ClickToggle --> StandardMode
```
## Justification
An **Activity Diagram** models this best because it represents a strict state change in the UI layer driven by user control.
## Process Descriptions
- **ApplyCSSMirror**: Reverses the video feed horizontally so right-handed instructors look left-handed.
- **SwapText**: A regex function that dynamically alters the pattern instructions to prevent cognitive dissonance.
