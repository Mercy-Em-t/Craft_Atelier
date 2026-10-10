# UC-05: Trigger Panic Button SOS - Scenarios

## Scenario Analysis Table

| Scenario Type | ID | Description | Outcome |
|---|---|---|---|
| **Main Scenario (Happy Path)** | MS-1 | Customer gets stuck, hits the red SOS button, video pauses, Ops Hub is alerted, and a WebRTC call resolves the issue. | **Success:** Goal achieved smoothly. |
| **Alternative** | ALT-1 | **Accidental Click:** Customer hits SOS, realizes it, and cancels the request within the 5-second countdown window. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-2 | **Audio-Only Fallback:** Customer has a weak connection; WebRTC downgrades from video to an audio-only call. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-3 | **Text Chat Pivot:** Customer prefers not to speak and switches the SOS interface to a live text chat. | **Success:** Goal achieved via alternate route. |
| **Alternative** | ALT-4 | **Queue Waiting:** All agents are busy; Customer is placed in a queue with an estimated wait time. | **Success:** Goal achieved via alternate route. |
| **Exception** | EXC-1 | **Camera Permissions Denied:** Browser blocks WebRTC; system falls back to a WhatsApp chat link. | **Failure:** Goal aborted or requires manual intervention. |
| **Exception** | EXC-2 | **Agent Timeout:** No agent answers within 2 minutes; system creates an urgent offline support ticket. | **Failure:** Goal aborted or requires manual intervention. |
