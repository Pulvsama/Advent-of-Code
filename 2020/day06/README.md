# Day 6: Custom Customs

## Problem Summary

Groups of people answered "yes" to customs declaration questions (labeled `a` through `z`). Each group's answers are separated by blank lines, with each person's answers on a separate line.

## Solution

### Part 1 - Count Any "Yes"
Count the number of questions to which **anyone** in each group answered "yes", then sum across all groups.

**Approach:** For each group, combine all answers into a single string and use a `set` to find unique characters.

### Part 2 - Count Everyone "Yes"
Count the number of questions to which **everyone** in each group answered "yes", then sum across all groups.

**Approach:** Use `set.intersection()` across all members' answers in each group to find common "yes" responses.

```bash
python solution.py
```