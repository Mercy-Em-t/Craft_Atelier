# UC-03: Create Modular SKU - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Creator drags 3 yarn colors and 1 hook into the builder, COGS is calculated, margin is set, and a new Kit is published to the catalog. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Draft Saving:** Creator builds the kit but saves it as a draft to publish next week. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Custom Margin:** Creator overrides the default 15% margin to 25%, dynamically updating the retail price. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Variant Creation:** Creator duplicates an existing kit and just swaps one yarn color to save time. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Pattern Upload:** Creator uploads a custom PDF pattern to be bundled digitally with the physical materials. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Missing Components:** Creator tries to publish a kit with no yarn selected; system prevents publishing. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Discontinued Material:** Creator selects a yarn color that is flagged as 'Discontinued' in the raw_materials DB. | **Failure:** Goal aborted or requires manual intervention. |
