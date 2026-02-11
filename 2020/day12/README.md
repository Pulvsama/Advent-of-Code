# Day 12: Rain Risk

## Problem Summary

Navigate a ship using instructions for movement (N/S/E/W), rotation (L/R), and forward movement (F). Calculate the Manhattan distance from the starting position after all instructions. Part 2 introduces waypoint-relative navigation.

## Solution

### Part 1 - Direct Ship Navigation
The ship faces a direction and moves according to instructions. Rotations change the ship's facing direction.

**Approach:** Track ship position and current facing direction. Use modular arithmetic on `'NESW'` string for rotations, and apply directional deltas for movement.

### Part 2 - Waypoint Navigation
Instructions now move a waypoint relative to the ship. `F` moves the ship toward the waypoint, while rotations spin the waypoint around the ship.

**Approach:** Track both ship and waypoint positions. For rotations, apply coordinate transformation: `(x, y) → (-y, x)` for 90° right turns. Multiply waypoint offset by `F` value for ship movement.

```bash
python solution.py
```