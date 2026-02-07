# Day 10: Adapter Array

## Challenge Description
Chain together joltage adapters that can connect to sources within 1-3 jolts of their rating to power a device. Find the distribution of joltage differences and calculate the total number of valid adapter arrangements.

## Approach

### Part 1: Joltage Distribution Analysis
- Sort adapters and compute differences between consecutive elements
- Track frequency of 1-jolt and 3-jolt differences
- **Complexity:** O(n log n) due to sorting

### Part 2: Counting Valid Arrangements
- Applied **dynamic programming** with memoization
- For each adapter, calculate total paths by summing ways to reach it from adapters within 1-3 jolts lower
- Built solution iteratively from charging outlet (0 jolts) to device
- **Complexity:** O(n) after initial sort

## Key Techniques
- **Bottom-up dynamic programming** for combinatorial counting
- Dictionary-based memoization for efficient lookups
- Recognizing recurrence relation: `ways[n] = ways[n-1] + ways[n-2] + ways[n-3]`

## Example
```
Input: [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
Sorted chain: 0 → 1 → 4 → 5 → 6 → 7 → 10 → 11 → 12 → 15 → 16 → 19 → 22

Part 1: 7 differences of 1-jolt × 5 differences of 3-jolt = 35
Part 2: 8 distinct valid arrangements
```

## Learning Outcomes
- Recognizing when problems require **combinatorial counting** vs. simple optimization
- Applying dynamic programming to graph path counting problems
- Efficient use of dictionaries for sparse memoization
- Understanding how small constraint changes (1-3 jolt window) enable tractable solutions
