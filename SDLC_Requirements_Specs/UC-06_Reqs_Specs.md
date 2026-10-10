# UC-06: Left-Handed Mirror

**Kano Priority:** 13. Attractive

---

## Requirement 1
> **The Left-Handed Customer views the tutorial in a spatial orientation that matches their dominant hand.**

### System Specifications
1. The System shall listen for a toggle event on the 'Left-Handed Mode' switch.
2. The System shall apply a CSS transform `scaleX(-1)` to the video container.
3. The System shall execute a regex replacement on textual instructions, swapping 'left' with 'right'.

### World-Machine Interface Mapping
- **Environmental Phenomenon (The World):** The user holding the crochet hook in their left hand instead of their right.
- **Interface Phenomenon (The Machine):** The manipulation of the browser's CSSOM (CSS Object Model).

### Assumptions (Domain Properties)
*For the System meeting the Specification to successfully satisfy the Requirement, the following must hold true in the real world:*
- **A1:** The video was shot directly top-down so that mirroring it perfectly reflects left-handed mechanics.
- **A2:** The user understands that the text has been automatically swapped for them.
