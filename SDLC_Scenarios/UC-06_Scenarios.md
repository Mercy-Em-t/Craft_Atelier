# UC-06: Toggle Left-Handed Mirror - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Left-handed user clicks the toggle, CSS mirror transform is applied to the video, and directional text is swapped (Left -> Right). | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Mid-Tutorial Toggle:** User realizes they need mirror mode on Step 4 and toggles it without losing their place. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Persistent Preference:** User's profile saves the toggle state so future tutorials default to Left-Handed. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Text-Only Reversion:** User likes the mirrored video but wants standard text; they uncheck 'Swap Text'. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Slow Connection:** CSS loads instantly, but video buffer resets smoothly. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Regex Text Failure:** Complex pattern text is poorly formatted and the 'Left/Right' string swap creates gibberish. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Browser Incompatibility:** Extremely old browser ignores CSS `transform: scaleX(-1)` property. | **Failure:** Goal aborted or requires manual intervention. |
