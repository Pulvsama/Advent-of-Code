# Advent of Code 2020 - Day 01: Report Repair

## Problem
Find entries in an expense report that sum to **2020**, then multiply them together.

- **Part 1**: Find two numbers that sum to 2020
- **Part 2**: Find three numbers that sum to 2020

## Approach & Complexity Analysis

### Two-Sum (Part 1)

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Hash Set | O(n) | O(n) |

The **hash set approach** trades memory for speed—storing seen values allows O(1) complement lookups.

### Three-Sum (Part 2)

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Reduce to Two-Sum | O(n²) | O(n) |

For each element, the problem reduces to a two-sum on the remaining array.

## Performance Benchmark

Benchmarked on randomly generated test cases with guaranteed solutions:

![Time Comparison](Time%20graph.png)

**Key Observations:**
- Hash set method stays nearly flat (linear time)
- Brute force in O(n²) is growing way faster than set method
- Three-sum follows expected O(n²) behavior

## Files

- `solution.py` — Clean implementation of both parts
- `additional.py` — Benchmarking script with test case generation
