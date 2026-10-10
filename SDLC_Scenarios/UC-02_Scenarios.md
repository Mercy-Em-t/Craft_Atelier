# UC-02: Bulk Address CSV Upload - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | HR Manager uploads a perfectly formatted CSV of 50 addresses, system calculates bulk total, Manager pays, and 50 tracking IDs are generated. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Partial Correction:** System flags 2 rows with bad phone numbers, Manager fixes them in the UI without re-uploading. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Template Download:** Manager downloads the blank CSV template before filling and uploading. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Split Invoicing:** Manager pays for 25 kits today and saves the remaining 25 in a drafted batch. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Duplicate Detection:** System detects duplicate employee phone numbers and prompts Manager to merge or keep. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Invalid Format:** Uploaded file is a PDF instead of a CSV; system rejects immediately. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Payment Limit Exceeded:** Bulk total exceeds M-Pesa transaction limit; transaction fails. | **Failure:** Goal aborted or requires manual intervention. |
