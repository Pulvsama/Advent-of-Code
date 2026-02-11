# Day 7: Handy Haversacks

## Problem Summary

Given luggage rules defining which colored bags must contain other colored bags (with quantities), determine how many bag colors can eventually contain a "shiny gold" bag, then calculate how many individual bags are required inside one "shiny gold" bag.

## Solution

### Part 1 - Container Search
Find all bag colors that can contain a "shiny gold" bag (directly or indirectly).

**Approach:** Build a reverse adjacency graph mapping each bag color to colors that can contain it, then traverse from "shiny gold" using BFS/DFS to count all reachable containers.

### Part 2 - Total Bag Count
Count the total number of bags required inside a single "shiny gold" bag.

**Approach:** Build a forward adjacency graph with (color, count) tuples, then use **recursive DFS** to multiply counts through the nested structure and sum all contained bags.

```bash
python solution.py
```
