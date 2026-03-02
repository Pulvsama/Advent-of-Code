# Day 19: Monster Messages

## Problem Summary

Given a set of numbered grammar rules and a list of messages, determine how many messages fully match rule `0`.
Part 2 introduces recursive-style updates to rules `8` and `11`, requiring a practical strategy to validate messages without brute-force parsing.

## Solution

### Part 1 - Compile Rules into Regex
Convert the rule graph into a single regular expression and count messages that match it from start to end.

**Approach:** Build regex fragments recursively with memoization (cache) so each rule is expanded once, then compile `^rule_0$` and test every message.

### Part 2 - Handle Recursive Rule Updates
Adapt to recursive behavior by approximating recursion depth with bounded expansions for rules `8` and `11`, then rebuild and reuse the same regex-matching pipeline.

**Approach:** Generate multiple alternatives for repeating rule patterns (e.g., `42^n` and `42^n31^n`) for reasonable `n`, which captures valid inputs efficiently for the puzzle dataset.

## Techniques Used

- Recursive rule expansion with memoization for fast pattern construction.
- Dynamic regex composition for context-free-like rule sets.
- Bounded unrolling to handle recursion pragmatically under input constraints.
- Anchored matching to enforce full-string validity (not partial matches).

## Example

Input (rules + messages excerpt):

```text
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
```

Output:

```text
Part 1 valid messages: 1
```

## Key Takeaways

- Complex rule systems can often be transformed into efficient pattern-matching problems.
- Memoization is a high-impact optimization for recursive dependency graphs.
- When exact recursion is costly, bounded expansion can be a practical and reliable engineering tradeoff.

```bash
python solution.py
```
