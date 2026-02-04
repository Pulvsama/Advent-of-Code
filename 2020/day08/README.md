# Day 8: Handheld Halting

## Challenge Overview

Execute a handheld console program that detects infinite loops and identifies the accumulator value before the loop occurs (Part 1). Fix a single corrupted instruction by swapping `jmp`/`nop` to make the program terminate normally (Part 2).

---

## Approach

| Part | Problem | Algorithm |
|------|---------|-----------|
| **Part 1** | Detect infinite loop; report accumulator | **Cycle Detection with Visited Set** |
| **Part 2** | Fix program corruption; find valid state | **Brute-Force Instruction Mutation + Cycle Detection** |

### Key Algorithm: Cycle Detection

Track visited instruction indices in a set. If we attempt to execute an instruction twice, we've hit an infinite loop. This simple mechanism elegantly solves Part 1 in a single pass.

### Part 2 Strategy

**Iterate through each `jmp`/`nop` instruction, flip it, and test**:
- Create a modified instruction list
- Run cycle detection on the mutated program
- Return the accumulator if the program terminates normally (no cycle)

This brute-force approach is efficient for small instruction sets and guarantees finding the one corrupted instruction.

---

## Example

**Input Program:**
```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

**Part 1 Execution Trace:**
```
[0] nop +0  → acc=0, next=1
[1] acc +1  → acc=1, next=2
[2] jmp +4  → acc=1, next=6
[6] acc +1  → acc=2, next=7
[7] jmp -4  → acc=2, next=3
[3] acc +3  → acc=5, next=4
[4] jmp -3  → acc=5, next=1
[1] acc +1  → VISITED AGAIN! → acc=5 (Part 1 Answer)
```

**Part 2:** Swap instruction [4] from `jmp -3` to `nop -3`. Program terminates with `acc=8`.

---

## Techniques & Optimizations

- **Visited Set Tracking:** $O(1)$ lookups detect cycles without scanning history. Avoids redundant list operations.
- **Tuple Unpacking:** Clean parsing of operation and argument into `(op, arg)` pairs.
- **List Copying:** Shallow copy of instruction list for mutation testing (lightweight and sufficient for small programs).
- **Early Termination:** Part 2 stops immediately upon finding a valid solution, avoiding exhaustive search.

---

## Key Takeaways

- **Cycle detection** is fundamental to many problems; a simple visited set often suffices.
- **Mutation testing** combined with a robust test harness (the `run()` function) enables efficient searching.
- **Separation of concerns:** The `run()` function encapsulates execution logic, making both parts clean and maintainable.
- **Type hints** (`List[Tuple[str, str]]`, return types) improve readability and enable IDE/linter support.

---

## Complexity

| Part | Time | Space |
|------|------|-------|
| Part 1 | O(n) | O(n) |
| Part 2 | O(n²) | O(n) |

*n = number of instructions*

---

## Usage

```bash
python solution.py
```

---