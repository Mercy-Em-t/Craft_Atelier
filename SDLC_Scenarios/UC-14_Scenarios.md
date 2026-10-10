# UC-14: Generate Tax CSV - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Accountant selects the month of October, clicks export, system formats data to KRA e-TIMS schema, and downloads the file. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Quarterly Export:** Accountant selects a 3-month date range for quarterly filing. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Zero-Sales Month:** Accountant runs export for a month with no sales; system generates a valid CSV with only headers. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Refund Exclusion:** System automatically deducts fully refunded orders from the Gross Sales column. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Automated Email:** Accountant schedules the report to automatically email to the CFO on the 1st of every month. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Schema Mismatch:** KRA adds a new mandatory column overnight; generated CSV is rejected by the government portal. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Data Corruption:** An old order lacks a timestamp; the export script throws a NullReferenceException. | **Failure:** Goal aborted or requires manual intervention. |
