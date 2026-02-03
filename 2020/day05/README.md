# Advent of Code 2020 - Day 5: Binary Boarding

## Problem Summary

Decode boarding passes that use **binary space partitioning** to specify seats on an airplane:
- First 7 characters (`F`/`B`) determine the **row** (0-127)
- Last 3 characters (`L`/`R`) determine the **column** (0-7)
- Seat ID = `row * 8 + column`

## Solution Approach

### Part 1: Find the Highest Seat ID

The boarding pass characters directly map to binary:
- `F` → `0`, `B` → `1` (rows)
- `L` → `0`, `R` → `1` (columns)

Convert each pass to binary, compute the seat ID, and track the maximum.

### Part 2: Find Your Seat

Your seat is the only missing one in the list (with occupied neighbors on both sides).

1. Collect all seat IDs
2. Sort them
3. Find the gap — where two consecutive IDs differ by 2

## Usage

```bash
python solution.py
```

Outputs:
- **Part 1**: Highest seat ID on any boarding pass
- **Part 2**: Your seat ID (the missing one in the sequence)
