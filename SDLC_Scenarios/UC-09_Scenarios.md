# UC-09: Batch Dispatch Orders - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Dispatcher selects 5 packed orders going to Kilimani, assigns Boda Rider 'John', system generates 5 PINs and sends 5 WhatsApp alerts. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Single Dispatch:** Dispatcher assigns just 1 highly urgent VIP order to a dedicated rider. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Rider Re-assignment:** John's bike breaks down in the parking lot; Dispatcher swaps the batch to Rider 'Mary'. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Geo-Sorting:** Dispatcher uses the UI to automatically group orders by neighborhood radius. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Manual WhatsApp Trigger:** API limits hit, Dispatcher clicks a button to manually trigger fallback SMS for the PINs. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **WhatsApp API Ban:** Meta blocks the business number; Customers never receive their Delivery PINs. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Rider No-Show:** Selected Boda Rider never arrives; batch sits on the loading dock indefinitely. | **Failure:** Goal aborted or requires manual intervention. |
