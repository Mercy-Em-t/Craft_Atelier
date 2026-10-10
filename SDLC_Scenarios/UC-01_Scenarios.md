# UC-01: Checkout & Pay - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Customer enters valid phone number, receives STK push, enters M-Pesa PIN, and the system verifies the callback and confirms the order. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Gifter Checkout:** Customer inputs a separate delivery phone number for the tracking SMS. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Cart Modification:** Customer changes quantities on the checkout page before initiating payment. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Manual Paybill:** STK push fails, so the customer manually pays via the Paybill menu and inputs the transaction code. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Session Restore:** Customer accidentally closes tab, returns, and cart is restored via local storage. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Insufficient Funds:** Daraja API callback returns failure, order is aborted, and customer is prompted to retry. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Daraja API Outage:** System cannot reach Safaricom; checkout is disabled with an error message. | **Failure:** Goal aborted or requires manual intervention. |
