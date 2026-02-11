# Day 8: Handheld Halting

## Problem Summary

Simulate a simple assembly-like program with three instructions (`acc`, `jmp`, `nop`). Detect when the program enters an infinite loop and report the accumulator value. Then, fix a single corrupted instruction to make the program terminate normally.

## Solution

### Part 1 - Infinite Loop Detection
Run the program and detect when any instruction is executed twice, returning the accumulator value at that moment.

**Approach:** Use a `set` to track visited instruction indices. Stop execution when revisiting an index, indicating an infinite loop.

### Part 2 - Fix Corruption
Find which single `jmp` or `nop` instruction is corrupted and should be swapped to allow the program to terminate.

**Approach:** **Brute-force** by trying each `jmp`/`nop` swap, running the modified program with cycle detection, and returning the accumulator when a version terminates normally.

```bash
python solution.py
```
