# UC-10: Input Delivery PIN - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Rider arrives, asks Customer for PIN, calls Dispatcher, Dispatcher types PIN into Hub, system verifies, and order is DELIVERED. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Customer Reads PIN via Window:** Customer is quarantined, holds PIN up to window, Rider reads it to Dispatcher. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Neighbor Proxy:** Customer isn't home, calls neighbor to accept box, sends neighbor the PIN. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Dispatcher Typo:** Dispatcher types 1235 instead of 1234, system rejects, Dispatcher corrects it immediately. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **SMS Fallback:** Rider's phone battery dies, Dispatcher verifies PIN by having customer text it to the main business line. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Wrong PIN Lockout:** Dispatcher enters incorrect PIN 3 times; order locks and requires Admin override. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Customer Lost PIN:** Customer deleted the WhatsApp message and cannot provide the PIN; Rider must return the box. | **Failure:** Goal aborted or requires manual intervention. |
