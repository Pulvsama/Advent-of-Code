# Day 17: Conway Cubes

## Problem Summary

Simulate Conway's Game of Life in 3D and 4D for six cycles, starting from a 2D input slice. Count active cubes after the sixth cycle for each dimension.

## Solution

### Part 1 - 3D Simulation
Track active cubes in a set of `(x, y, z)` coordinates. For each cycle, build a set of cubes to check (all active cubes and their neighbors), count active neighbors, and apply the rules to produce the next state.

### Part 2 - 4D Simulation
Extend the state to `(x, y, z, w)` and reuse the same rules with 4D neighbor offsets. Run six cycles and count active cubes.

```bash
python solution.py
```
