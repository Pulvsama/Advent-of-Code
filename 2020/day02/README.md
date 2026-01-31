# Advent of Code 2020 - Day 2: Password Philosophy

## Problem Summary

Given a list of passwords with their policies, determine how many passwords are valid.

Each line contains: a policy (two numbers and a letter) and a password.

## Solution

### Part 1 - Character Count Policy

The two numbers represent the **minimum and maximum** times the specified letter must appear in the password.

**Approach:** Count occurrences of the letter and check if it falls within the given range.

### Part 2 - Positional Policy

The two numbers represent **positions** (1-indexed) where **exactly one** must contain the specified letter (XOR logic).

**Approach:** Check if the letter appears at exactly one of the two positions using a logical XOR comparison.

## Usage

```bash
python solution.py
```

Both parts are solved by parsing the input once and applying the respective validation rules.
