# Day 13: Shuttle Search

## Problem Summary

Given a bus schedule with buses departing at different intervals (IDs represent departure frequencies), find the earliest bus you can catch after a given timestamp. Then, determine the earliest timestamp where buses depart at specific sequential offsets.

## Solution

### Part 1 - Earliest Departure
Find the bus with the shortest wait time after the given timestamp, then return the product of the bus ID and wait time.

**Approach:** Use modular arithmetic `(-timestamp) % bus_id` to calculate the wait time for each bus in service, tracking the minimum.

### Part 2 - Sequential Departures
Find the earliest timestamp where each bus departs at a specific offset (e.g., bus at index `i` departs at time `t + i`).

**Approach:** Apply the **Chinese Remainder Theorem** by iteratively building the solution—find when each constraint is satisfied, then use the product of satisfied bus IDs as the step size to maintain all previous constraints while searching for the next.

```bash
python solution.py
```
