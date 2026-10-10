# UC-16: Disburse Creator Royalties - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Admin clicks 'Disburse All', system calculates totals, triggers M-Pesa B2C payments, and resets Creator balances to zero. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Single Disbursement:** Admin clicks 'Disburse' next to just one specific Creator instead of running the global batch. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Minimum Threshold:** System skips any Creator whose pending balance is under KES 500 to save on transfer fees. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **SMS Receipt:** Creator receives an automated SMS confirming the exact amount transferred to their phone. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Manual Override:** Admin manually marks a payout as 'Paid via Cash' for a Creator without M-Pesa. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **B2C Insufficient Funds:** The company's M-Pesa account doesn't have enough money; transactions fail. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Invalid Creator Phone:** Creator registered a phone number that is blocked from receiving money; transaction reverses. | **Failure:** Goal aborted or requires manual intervention. |
