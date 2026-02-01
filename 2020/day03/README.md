# Day 3: Toboggan Trajectory

## Problem Summary

Given a map of trees (represented as `#`) and open squares (`.`), count how many trees you encounter while traversing the map following specific slopes. The map repeats horizontally infinitely.

## Solution

### Part 1
Count trees encountered when moving **3 right, 1 down** from the top-left corner until reaching the bottom.

**Approach:** Instead of duplicating the forest horizontally, use modular arithmetic (`j = (3 * i) % width`) to wrap around when exceeding the map's width.

### Part 2
Count trees for multiple slopes and multiply the results together:
- Right 1, Down 1
- Right 3, Down 1
- Right 5, Down 1
- Right 7, Down 1
- Right 1, Down 2

**Approach:** Generalized the Part 1 function to accept any slope `(x, y)`, adjusting the row step and column calculation accordingly.

## Key Techniques
- **Cyclic indexing** with modulo to handle infinite horizontal repetition
- **Parameterized slopes** for flexibility in Part 2

## Usage
```bash
python solution.py
```
