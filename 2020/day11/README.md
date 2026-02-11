# Day 11: Seating System

## Problem Summary

Simulate people choosing seats in a ferry waiting area based on occupancy rules. Apply rules repeatedly until the seating pattern stabilizes, then count occupied seats. Part 1 uses adjacent neighbors; Part 2 uses line-of-sight visibility.

## Solution

### Part 1 - Adjacent Seat Rules
People sit if no adjacent seats are occupied and leave if 4+ adjacent seats are occupied. Simulate until stable.

**Approach:** For each iteration, create a new grid by checking the 8 adjacent neighbors of each seat. Stop when no seats change state.

### Part 2 - Line-of-Sight Rules
People now check the first visible seat in each of 8 directions (not just adjacent). Leave threshold increases to 5+ visible occupied seats.

**Approach:** For each seat, scan outward in 8 directions until hitting a seat (ignoring floor spaces). Apply new rules until convergence.

```bash
python solution.py
```
