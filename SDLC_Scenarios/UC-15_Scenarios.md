# UC-15: View Royalty Dashboard - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Creator logs in, views a 30-day line chart of their kit sales, and checks their 'Pending Payout' balance. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **All-Time View:** Creator zooms out the chart to see their sales volume over the entire year. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Mobile View:** Creator checks the dashboard on their phone; CSS flexbox stacks the charts vertically. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Multiple SKUs:** Creator has 3 different kits; they toggle visibility to compare the performance of each kit. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Download Statement:** Creator downloads a PDF receipt of all past payouts for their personal taxes. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **RLS Failure:** Creator's JWT token expires; dashboard loads completely blank. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Chart Rendering Error:** Browser fails to load the Chart.js library; user only sees raw text numbers. | **Failure:** Goal aborted or requires manual intervention. |
