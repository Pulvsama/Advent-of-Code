# Day 23: Crab Cups

## Problem Summary

Simulate a cup-shuffling game where a crab rearranges cups in a circle. Each move, three cups are picked up from the circle and re-inserted after a calculated destination cup. Part 1 runs 100 moves on 9 cups; Part 2 scales to **1,000,000 cups** and **10,000,000 moves**.

## Solution

### Part 1 - Small Circle
Simulate 100 moves on the original 9-cup circle and read the cup order after cup `1`.

**Approach:** Model the circle as a **linked list via an array** (`next_cup[i]` stores the cup clockwise of cup `i`), enabling O(1) pickups and insertions per move.

### Part 2 - Massive Scale
Extend the circle to 1,000,000 cups, run 10,000,000 moves, and return the product of the two cups immediately clockwise of cup `1`.

**Approach:** The same linked-list array scales linearly — no node objects or pointer overhead, just a flat integer array for cache-friendly access.

### Example

```
Input:  389125467

Move 1: current = 3 → pick up [8, 9, 1] → destination = 2
Cups:   3  2  8  9  1  5  4  6  7

Move 2: current = 2 → pick up [8, 9, 1] → destination = 7
Cups:   3  2  5  4  6  7  8  9  1
...
```

## Key Techniques

- **Array-based linked list:** Using `next_cup[i] = j` to represent the circular structure avoids the overhead of dictionaries or node objects, making millions of iterations feasible in pure Python.
- **Wraparound trick:** `destination = current - 1 or max_val` concisely handles the wrap from cup `1` back to the highest cup.

## Takeaways

- Choosing the right data structure is everything — a naive list with `insert`/`pop` would be O(n) per move, making Part 2 infeasible. The array-backed linked list keeps each move O(1).
- Python can handle 10M iterations efficiently when the inner loop is tight and avoids object allocation.

```bash
python solution.py
```