# UC-05: Trigger Panic Button

**Kano Priority:** 12. Attractive

---

## Requirement 1
> **The Customer receives immediate human intervention when they are hopelessly stuck.**

### System Specifications
1. The System shall render a persistent red SOS button overlay on the video.
2. The System shall pause the video element when the button is clicked.
3. The System shall initiate a WebRTC connection request to the Operations Hub.
4. The System shall transmit the user's current tutorial step ID to the Support Agent.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The user experiencing frustration and verbally requiring help.
- **Interface Phenomenon (The Machine):** The negotiation of ICE candidates via the WebRTC protocol.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The user grants the browser permission to access their microphone/camera.
- **A2:** A Support Agent is actively monitoring the dashboard to receive the call.
