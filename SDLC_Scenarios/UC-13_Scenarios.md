# UC-13: View Financial/Audit Logs - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Admin queries logs for a specific order ID, system returns an immutable chronological timeline of all status changes and users. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Date Range Filter:** Admin views all 'PACKED' events between Monday and Friday to calculate warehouse throughput. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **User Filter:** Admin filters logs by a specific Packer's ID to review their error rate. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **CSV Export:** Admin clicks 'Export' and downloads the visual table as a raw CSV for Excel analysis. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Financial Snapshot View:** Admin expands an order log to see exactly what the subtotal/tax was on that specific day. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Query Timeout:** Admin tries to load 5 years of logs at once; Supabase terminates the query. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Unauthorized Access:** Junior Support Agent tries to view financial logs; RLS blocks the query. | **Failure:** Goal aborted or requires manual intervention. |
