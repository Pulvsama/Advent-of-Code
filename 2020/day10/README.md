# Day 10: Adapter Array

## Problem Summary

Chain joltage adapters together from the charging outlet to your device. Each adapter can connect to sources within 1-3 jolts of its rating. Calculate the distribution of joltage differences, then count all valid adapter arrangements.

## Solution

### Part 1 - Joltage Difference Distribution
Sort all adapters, compute differences between consecutive adapters, and return the product of 1-jolt and 3-jolt difference counts.

**Approach:** Sort the adapters, add the outlet (0) and device (max+3), then count differences with a simple loop and multiplication.

### Part 2 - Count Valid Arrangements
Determine how many distinct valid adapter arrangements exist.

**Approach:** Use **dynamic programming** to count paths. For each adapter, sum the ways to reach it from adapters 1-3 jolts lower: `ways[n] = ways[n-1] + ways[n-2] + ways[n-3]`. Build solution bottom-up from outlet to device.

```bash
python solution.py
```
