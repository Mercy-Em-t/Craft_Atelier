# UC-04: Interactive Tutorial

**Kano Priority:** 11. One-Dimensional

---

## Requirement 1
> **The Beginner watches a looping instructional video and advances only when ready.**

### System Specifications
1. The System shall instantiate an HTML5 video player.
2. The System shall loop a specific timestamp range (e.g., 1:00 to 1:15) continuously.
3. The System shall provide 'Next' and 'Previous' buttons that update the timestamp range variable.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The user attempting to physically mimic the crochet stitch with their hands.
- **Interface Phenomenon (The Machine):** The DOM manipulation of the HTML5 video element's `currentTime` property.

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The user's device has a functional screen and hardware decoding for video playback.
- **A2:** The timestamps provided in the database accurately map to the physical stitches.
