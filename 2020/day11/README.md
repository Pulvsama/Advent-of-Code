## Day 11: Seating System

This challenge simulates seat occupancy in a ferry waiting area using rule-based updates. The task is to apply the rules until the layout stabilizes and report the number of occupied seats.

### Approach
- Model the grid as immutable iterations: compute the next layout from the current layout until no cells change.
- Part 1 uses immediate neighbors; Part 2 uses line-of-sight neighbors in eight directions with a visibility scan.
- Track occupied counts per iteration and stop on convergence.

### Techniques Used
- Efficient neighbor enumeration with precomputed direction vectors.
- Early exit when a layout pass produces no changes.
- Clean separation of parsing, stepping, and convergence detection to keep the logic testable.

### Key Takeaways
- Iterative simulation is easier to reason about with immutable state transitions.
- Precomputing directional scans simplifies the rule engine and improves performance.
- Clear separation of concerns makes complex rule sets easier to extend and verify.
