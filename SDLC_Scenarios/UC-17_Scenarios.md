# UC-17: Review Support Escalations - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Support Agent opens ticket, views the chronological order history and assigned Packer, and resolves the customer's missing item complaint. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Rider Contact:** Agent clicks the Rider's name to instantly reveal their phone number and calls them. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Ticket Transfer:** Agent cannot solve the issue and re-assigns the ticket to a Senior Manager. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Customer History:** Agent clicks the Customer's profile and sees they have successfully received 5 previous orders. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Tagging:** Agent tags the ticket as 'Refund Needed' to automatically ping the Finance Admin. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Missing Logs:** A bug prevented the delivery PIN from logging; Agent has no proof of delivery. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Angry Customer Hangs Up:** Customer disconnects the WebRTC call before the Agent can gather the order ID. | **Failure:** Goal aborted or requires manual intervention. |
