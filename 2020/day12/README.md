# Day 12: Rain Risk

## Problem Overview
Navigate a ship following a sequence of navigation instructions (forward, cardinal directions, rotations) and calculate the Manhattan distance to the destination. The twist: Part 2 changes the rule set, requiring understanding of waypoint rotation mechanics separate from ship movement.

## Approach & Algorithm

**Part 1:** Direct navigation with ship-centric rotation
- Map compass directions to coordinate deltas using a dictionary
- Track current heading and apply rotation using modular arithmetic (rotation angle ÷ 90°)
- Use circular list indexing to elegantly handle direction cycling: `'NESW'[index % 4]`

**Part 2:** Waypoint-based navigation (more complex)
- Introduce waypoint coordinates relative to ship (initially at 10E, 1N)
- Decouple ship movement from waypoint direction, rotating only the waypoint around the origin
- Implement 90° rotation using transformation matrices in a loop: `(x, y) → (-y, x)` for right rotation
- Accumulate final position and calculate Manhattan distance

## Example

**Input:**
```
F10   (Forward 10 units)
N3    (Move North 3)
F7    (Forward 7 units)
R90   (Rotate right 90°)
F11   (Forward 11 units)
```

**Part 1 Output:** `25` (Manhattan distance after following original rules)  
**Part 2 Output:** `286` (Different mechanics, same example result)