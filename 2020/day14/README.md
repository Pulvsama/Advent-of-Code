# Day 14: Docking Data

## Problem Summary

Initialize a ferry docking program by executing mask and memory write operations. The bitmask modifies values before they're written to memory. Part 1 applies masks to values; Part 2 applies masks to memory addresses to write to multiple locations.

## Solution

### Part 1 - Value Masking
Apply a 36-bit mask to values before writing to memory. Mask bits: '0' or '1' overwrite the value bit, 'X' leaves it unchanged.

**Approach:** Convert the mask to AND and OR operations. Replace 'X' with '1' for AND mask (preserves bits) and '0' for OR mask (overwrites bits). Apply both masks to each value before storing.

### Part 2 - Address Masking
Apply mask to memory addresses instead. Mask bits: '0' leaves address bit unchanged, '1' overwrites with 1, 'X' creates floating bits that generate all combinations.

**Approach:** Apply the mask to convert the address to a template with 'X' bits. Generate all possible addresses by replacing each 'X' with both '0' and '1' using itertools.product. Write the value to all resulting addresses.

```bash
python solution.py
```
