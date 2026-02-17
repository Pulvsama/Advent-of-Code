# Day 16: Ticket Translation

## Problem Summary

Parse field rules, your ticket, and nearby tickets. Part 1 asks for the scanning error rate by summing invalid values. Part 2 determines which field name maps to each ticket column, then multiplies the values on your ticket for fields starting with "departure".

## Solution

### Part 1 - Scanning Error Rate
Collect all rule ranges, merge them, and use binary search to check each nearby ticket value. Sum any value that is outside every valid range.

### Part 2 - Field Mapping
Filter out invalid nearby tickets first. For each column, test which rules match all values and build a list of possible names. Resolve the mapping by repeatedly fixing columns with a single remaining name and removing that name from other columns. Finally, multiply the "departure" fields from your ticket.

```bash
python solution.py
```
