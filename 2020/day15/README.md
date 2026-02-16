# Day 15: Rambunctious Recitation

## Problem Summary

Play a memory game with starting numbers where each turn speaks either 0 (if the previous number was new) or the age (turns since last spoken). Find the number spoken at specific turns.

## Solution

### Part 1 - 2020th Number
Find the 2020th number spoken in the game.

**Approach:** Use a dictionary to track the last index where each number was spoken. For each turn, check if the previous number exists in memory to calculate the next number (difference between current turn and last occurrence, or 0 if new).

### Part 2 - 30000000th Number
Find the 30000000th number spoken in the game.

**Approach:** Same algorithm as Part 1, just running for significantly more iterations. The dictionary-based approach handles the large iteration count efficiently.

```bash
python solution.py
```
