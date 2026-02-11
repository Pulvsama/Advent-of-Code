# Day 9: Encoding Error

## Problem Summary

Analyze a stream of numbers to find the first value that isn't the sum of any two numbers in the previous 25 values (the preamble). Then, find a contiguous sequence of numbers that sum to this invalid number.

## Solution

### Part 1 - Find Invalid Number
Identify the first number that cannot be expressed as the sum of any two different numbers in the previous 25 values.

**Approach:** Use a **two-sum algorithm** with a hash set for each validation check, sliding the window through the sequence until finding a number that fails validation.

### Part 2 - Contiguous Sum Window
Find a contiguous sequence of at least two numbers that sum to the invalid number from Part 1, then return the sum of the smallest and largest numbers in that sequence.

**Approach:** Apply a **sliding window with two pointers**—expand the window when the sum is too small, contract when too large, and return `min + max` when the target is reached.

```bash
python solution.py
```