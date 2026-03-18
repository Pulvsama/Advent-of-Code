# Day 24: Lobby Layout

## Problem Summary

This puzzle models a hexagonal tile floor where each instruction path flips a tile between white and black. Part 1 asks for the number of black tiles after all flips, while Part 2 evolves the floor for 100 days using neighbor-based rules (a hex-grid cellular automaton).

## Solution

### Part 1 - Tile Flipping on a Hex Grid
Parse each direction string (`e`, `se`, `sw`, `w`, `nw`, `ne`) and walk from the origin to a target tile.

**Approach:** Represent tile positions with **axial coordinates** `(q, r)` and store black tiles in a `set`. Reaching the same tile toggles membership in the set, making each flip O(1) on average.

### Part 2 - 100-Day Simulation
Apply daily update rules based on black-neighbor counts: black tiles survive with 1 or 2 black neighbors; white tiles turn black with exactly 2 black neighbors.

**Approach:** For each day, evaluate only relevant tiles (current black tiles and their neighbors) instead of scanning an unbounded grid. This keeps the simulation focused and efficient.

### Example

```
Input lines:
esew
nwwswee

After parsing:
- "esew" lands on one tile and flips it to black
- "nwwswee" returns to origin and flips that tile

Black tiles after these two lines: 2
```

## Key Techniques

- **Axial coordinate system for hex grids:** Simplifies movement and neighbor math to fixed `(dq, dr)` offsets.
- **Set-based state representation:** Tracks only black tiles, enabling fast toggle and lookup operations.
- **Frontier evaluation:** Computes next state from a compact candidate set (`black + neighbors`) for better performance over 100 iterations.
- **Optional visualization tooling:** Includes plotting utilities for inspecting hex states during development and debugging.

## Takeaways

- Choosing the right coordinate system can turn a geometry-heavy problem into straightforward integer arithmetic.
- Sparse-state modeling (`set` of active tiles) is a strong pattern for automata on large or unbounded spaces.
- Constraining updates to the active frontier is a practical optimization that keeps Python simulations scalable.

```bash
python solution.py
```
