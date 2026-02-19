# Day 18: Operation Order

## Problem Summary

Evaluate many arithmetic expressions containing integers, `+`, `*`, and parentheses under two custom rule sets: (1) left-to-right evaluation with no normal precedence, and (2) addition having higher precedence than multiplication.

## Solution

### Part 1 - Left-to-Right Expression Evaluation
Compute each expression strictly from left to right, while still respecting nested parentheses.

**Approach:** Tokenize each expression and use a recursive parser that evaluates as it scans, applying the current operator immediately.

### Part 2 - Custom Precedence Parsing
Re-evaluate the same expressions, but now treat `+` as higher precedence than `*`.

**Approach:** Use precedence-aware recursive descent parsing (`parse_atom` + `parse(min_prec)`) so operator priority is controlled by code rather than Python's built-in evaluator.

## Techniques Used

- Recursive parsing for nested parenthetical expressions.
- Token-stream traversal with index tracking for deterministic evaluation.
- Custom operator-precedence handling (Pratt-style loop with `min_prec`).

## Example

Input expression:

```text
1 + 2 * 3 + 4 * 5 + 6
```

Output:

- Part 1 (left-to-right): `71`
- Part 2 (`+` before `*`): `231`

## Key Takeaways

- Turning ambiguous math rules into explicit parser logic is a strong algorithm-design exercise.
- Separating tokenization, atom parsing, and precedence logic improves correctness and maintainability.
- The same input can be solved under multiple rule systems by swapping only the evaluation strategy.

```bash
python solution.py
```
