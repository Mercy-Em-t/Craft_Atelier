# UC-08: Flag Stock Exception - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Packer spots damaged yarn, clicks 'Flag Exception', selects 'Damaged', order goes ON_HOLD, and Admin is alerted. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Missing Item Exception:** Packer selects 'Out of Stock' instead of 'Damaged' for an empty bin. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Admin Override:** Admin sees the alert, finds the yarn on a different shelf, and un-flags the order. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Partial Exception:** Order has 5 kits; only 1 kit is flagged, the other 4 are packed and wait in the box. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Exception Reversal:** Packer realizes they flagged the wrong order and instantly cancels the exception. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **System Timeout:** Exception payload fails to reach Supabase; Admin never receives the alert. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **False Positive:** Packer mistakenly flags an item as damaged when it is just a different dye lot. | **Failure:** Goal aborted or requires manual intervention. |
