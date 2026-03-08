# Day 22: Crab Combat

## Problem Summary

Two players play a card game (similar to War) with numbered decks. Each round, both draw their top card — the higher card wins and both cards go to the winner's deck. Part 2 introduces **Recursive Combat**, where sub-games are triggered when both players have enough cards remaining, and a history-based rule prevents infinite loops.

## Solution

### Part 1 - Classic Combat
Simulate the card game round by round until one deck is empty, then compute the winner's score using positional weights.

**Approach:** Use `deque` for O(1) popleft/append operations to model each player's deck efficiently.

### Part 2 - Recursive Combat
Simulate the game with recursive sub-games: if both players have at least as many remaining cards as their drawn card's value, the round winner is decided by a recursive sub-game on copied sub-decks. A **state memory set** of seen deck configurations prevents infinite recursion.

**Approach:** Recursive function with `set` of `(tuple, tuple)` snapshots for cycle detection. Sub-decks are sliced via `itertools.islice` to avoid unnecessary list copies.

### Example

```
Player 1: 9, 2, 6, 3, 1
Player 2: 5, 8, 4, 7, 10

Winner's score = 10×1 + 7×2 + 6×3 + 5×4 + 4×5 + 3×6 + 2×7 + 1×8 = 306
```

### Key Takeaways

- **`deque`** is the natural fit for queue-based card game simulations (O(1) double-ended ops vs O(n) list pops).
- **State hashing with tuples** provides a clean, hashable snapshot for cycle detection in recursive games.
- **`itertools.islice`** avoids materializing full sub-lists when slicing deques.

```bash
python solution.py
```