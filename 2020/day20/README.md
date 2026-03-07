# Day 20: Jurassic Jigsaw

## Problem Summary

Given a set of image tiles (each with a unique ID), reassemble them into a complete image by matching their edges. Part 1 asks for the product of the four corner tile IDs. Part 2 requires stitching the full image together and counting `#` cells that are **not** part of a sea monster pattern.

## Solution

### Part 1 - Reassemble the Grid
Find the arrangement of tiles such that all adjacent edges match, then multiply the IDs of the four corner tiles.

**Approach:** Precompute all 8 orientations (4 rotations + 4 flips) of every tile's edges. Build a **top map** — a dictionary mapping an edge string to all tile orientations that have that edge on top — enabling O(1) candidate lookup during placement. Solve the grid with recursive backtracking, placing tiles left-to-right, top-to-bottom, and pruning with edge constraints.

### Part 2 - Hunt the Sea Monster
Reconstruct the full image (borders stripped), then search all 8 orientations for a 20-wide, 3-tall sea monster pattern and subtract matched `#` cells from the total.

**Approach:** Map each placed tile back to its original pixel data, orient it to match the solved edge tuple, strip borders, and stitch rows together. Generate all rotations and reflections of the assembled image, then slide-window scan for the monster coordinates.

### Example Input
```
Tile 2311:          Tile 1951:
..##.#..#.          #.##...##.
##..#.....          #.####...#
#...##..#.          .....#..##
...                 ...
```
Each tile is a 10×10 grid. The solver matches edges across tiles to reconstruct the full picture.

## Techniques & Design Decisions

- **Edge hashing with a lookup map:** Instead of brute-force comparing every tile pair, edges are indexed in a `defaultdict(list)` so that finding compatible neighbours is O(1). A `left_map` was also built during preprocessing but turned out to be unnecessary — the backtracker places tiles left-to-right, so it first narrows candidates via `top_map` and then simply checks the left constraint inline. The top map alone provides enough pruning to keep the search fast.
- **Compact edge representation:** Edges are stored as plain strings (read left→right, top→bottom), and all 8 orientations are generated with a closed-form permutation list rather than repeated matrix rotations.
- **Recursive backtracking with early pruning:** Candidates are filtered by the top-edge constraint from the map, then immediately rejected if the left edge doesn't match — avoiding deep recursion into dead ends.
- **Pattern matching via coordinate offsets:** The sea monster is encoded as a list of `(row, col)` deltas, making the scan a simple membership check rather than regex or substring matching.

## Key Takeaways

- Precomputing a lookup structure (even a simple dictionary) can dramatically reduce search space in constraint-satisfaction problems.
- Not every precomputed structure ends up being used — the `left_map` was a reasonable investment that the algorithm's pruning strategy made redundant, a good reminder to profile before optimising further.
- Generating all orientations analytically (closed-form permutations) is cleaner and less error-prone than applying rotation/flip functions repeatedly.

```bash
python solution.py
```