# UC-04: View Interactive Tutorial - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Beginner opens the tutorial, the video auto-loops the first step, and they use the 'Next Step' button to progress through the pattern. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Voice Command:** Beginner says 'Next' aloud, and the system advances the video without touch. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Timestamp Scrubbing:** Beginner manually drags the video slider to re-watch a specific 3-second loop. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **State Resumption:** Beginner closes browser on Step 5, returns the next day, and the system resumes at Step 5. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Speed Adjustment:** Beginner slows the video playback to 0.5x speed to see the hook movement clearly. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Video Load Failure:** CDN is down; the system displays fallback static images and text instructions. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Hardware Decode Error:** Older smartphone cannot render the video; browser crashes. | **Failure:** Goal aborted or requires manual intervention. |
