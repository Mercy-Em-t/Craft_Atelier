# UC-07: Scan & Verify BOM - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Packer opens pending order, physically picks all items, taps them on the tablet checklist, UI flashes green, and order moves to PACKED. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Out of Order Scanning:** Packer taps the items in reverse order of the list; system still validates perfectly. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Barcode Fallback:** Packer uses the tablet camera to scan a barcode instead of manually tapping the screen. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Shift Handoff:** Packer goes on break mid-order; another Packer picks up the tablet and resumes the exact checklist state. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Multi-Kit Box:** Order contains 3 different kits; UI groups the checklists by kit to prevent confusion. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Missing Item:** Packer cannot find the required hook; cannot complete checklist (Order stuck). | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Tablet Sync Failure:** Warehouse WiFi drops exactly as the Packer finishes; tablet throws offline error. | **Failure:** Goal aborted or requires manual intervention. |
