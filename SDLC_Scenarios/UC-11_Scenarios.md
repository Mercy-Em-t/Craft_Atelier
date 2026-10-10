# UC-11: Update Business Settings - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Admin navigates to Settings, updates the M-Pesa Till Number, saves, and the Storefront cache is instantly invalidated. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Update Delivery Fee:** Admin changes the flat delivery rate from 200 to 250; all new checkouts reflect the price. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Toggle Maintenance Mode:** Admin flips a switch to 'ON'; Storefront displays 'Be right back' page. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Update Support Number:** Admin updates the WhatsApp support link URL in the header. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Revert Setting:** Admin realizes they made a typo in the Till number and uses the 'Undo' history button. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Invalid Till Format:** Admin tries to enter an 8-digit Till; system throws validation error. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Cache Invalidation Failure:** Edge network fails to clear; some customers see the old Till number. | **Failure:** Goal aborted or requires manual intervention. |
