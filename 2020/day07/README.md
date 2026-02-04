# Day 7: Handy Haversacks 

## Challenge Overview

Parse luggage rules defining nested bag requirements to determine (1) how many bag colors can eventually contain a "shiny gold" bag, and (2) how many individual bags are required inside a single "shiny gold" bag.

---

## Approach

| Part | Problem | Algorithm |
|------|---------|-----------|
| **Part 1** | Count bags that can contain shiny gold | **Reverse BFS**  traverse "contained by" relationships |
| **Part 2** | Count total bags inside shiny gold | **Recursive DFS**  multiply counts through nested structure |

### Data Structures

Built **two adjacency representations** from a single parse pass:
- `contained_by`: Maps each color  list of colors that can directly hold it (inverted graph for Part 1)
- `contains`: Maps each color  list of (color, count) tuples (forward graph for Part 2)

---

## Example

**Input:**
`
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
`

**Part 2 Calculation:**
`
shiny gold contains:
  1  dark olive     1  (1 + 3 + 4) = 8
  2  vibrant plum   2  (1 + 5 + 6) = 24
Total = 32 bags
`

---

## Techniques & Optimizations

- **Dual Graph Construction:** Single-pass parsing builds both forward and reverse adjacency lists, avoiding redundant file reads.
- **Regex-Based Parsing:** Used `re.split()` with escaped delimiters to handle pluralization variants (`bag`, `bags`, `bag,`, etc.).
- **Memoization-Ready DFS:** Recursive structure naturally handles the multiplicative counting; could add `@cache` for larger inputs.
- **Set-Based Visited Tracking:** Prevents double-counting in Part 1's BFS traversal.

---

## Key Takeaways

 **Graph modeling** transforms nested containment rules into traversable structures.  
 **Inverted adjacency lists** enable efficient "who contains me?" queries without full graph search.  
 **Recursive multiplication** elegantly solves nested counting: `count  (1 + nested_total)`.  
 Parsing complexity often dominatesrobust regex handling pays off for messy input formats.

---

## Complexity

| Part | Time | Space |
|------|------|-------|
| Part 1 | O(V + E) | O(V) |
| Part 2 | O(V + E) | O(V) recursion depth |

*V = bag colors, E = containment rules*

---

## Usage

`bash
python solution.py
`

---