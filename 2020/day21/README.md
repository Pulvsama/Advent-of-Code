# Day 21: Allergen Assessment

## Problem Summary

Each food label lists ingredients and possible allergens. The goal is to infer which ingredient contains which allergen, count how often allergen-free ingredients appear (Part 1), and produce the canonical dangerous ingredient list sorted by allergen name (Part 2).

## Solution

### Part 1 - Count Safe Ingredient Appearances
For each allergen, track the intersection of ingredients across all labels that mention it. Any ingredient left in these candidate sets may contain an allergen; all others are safe.

**Approach:** Build an allergen -> candidate ingredients map using set intersection, then repeatedly resolve single-candidate allergens and eliminate that ingredient from other candidate sets.

### Part 2 - Canonical Dangerous Ingredient List
Resolve the same allergen mapping fully, then output ingredients ordered by allergen name and joined by commas.

**Approach:** Use iterative constraint propagation (singleton elimination) until every allergen maps to exactly one ingredient.

### Example

Input:
```
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
```

Output:
```
Part 1: 5
Part 2: mxmxvkd,sqjhc,fvjkl
```

## Techniques & Design Decisions

- **Set intersections for candidate reduction:** Efficiently narrows possible ingredient-allergen mappings as each label is processed.
- **Constraint propagation:** Repeated singleton extraction removes ambiguity without brute-force search.
- **Defensive checks:** Explicit "no progress" and empty-candidate guards fail fast if input assumptions are violated.

## Key Takeaways

- Constraint-satisfaction problems often become straightforward when modeled with sets and elimination rules.
- A clean data model (allergen candidates + iterative pruning) keeps both parts readable and reusable.
- Small safety checks improve robustness and make debugging easier when assumptions break.

```bash
python solution.py
```
