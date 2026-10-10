# UC-12: Manage Global Inventory - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Inventory Manager uploads CSV of physical warehouse counts, system calculates deltas, updates the DB, and logs the shrinkage. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Manual Row Edit:** Manager notices one discrepancy and manually edits the stock integer via the UI instead of a CSV. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Zero Stock Trigger:** Upload sets a popular yarn to 0; system automatically hides it from the Storefront. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Positive Delta:** Manager uploads a count higher than the DB (found extra stock); system logs 'Found' instead of 'Shrinkage'. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Scheduled Count Reminder:** System alerts Manager it has been 30 days since the last full cycle count. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Concurrent Checkout:** A customer buys the last item exactly as the CSV is uploading; race condition corrupts the count. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Corrupted CSV:** File is encoded in UTF-16 instead of UTF-8; parser throws a fatal error. | **Failure:** Goal aborted or requires manual intervention. |
