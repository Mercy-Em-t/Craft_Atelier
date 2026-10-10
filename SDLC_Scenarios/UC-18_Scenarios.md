# UC-18: Process Customer Refund - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Support Agent inputs KES 500 partial refund, triggers M-Pesa B2C API, funds are returned to customer, and Creator ledger is adjusted. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Full Refund:** Agent clicks 'Refund Entire Order', returning all money and marking the order as CANCELED. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Store Credit Alternative:** Instead of fiat currency, Agent generates a 100% discount code for the customer's next purchase. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Ledger Deduction:** The KES 500 refund is automatically subtracted from the Creator's future royalty pool. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Reversal Sync:** The physical items in a fully refunded/canceled order are automatically added back to the `inventory` table. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **API Failure:** M-Pesa B2C API is down; the refund sits in a 'Pending' queue for 24 hours. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Fraudulent Refund:** A malicious Support Agent attempts to refund money to their own phone number. | **Failure:** Goal aborted or requires manual intervention. |
