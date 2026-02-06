# Day 9: Encoding Error

## Challenge Overview
This problem involves analyzing a stream of encrypted numbers to detect anomalies and identify vulnerable sequences. Part 1 requires finding the first number that doesn't follow a specific validation rule (sum of two previous numbers within a window), while Part 2 involves finding a contiguous sequence that sums to the vulnerable number.

## Approach

**Part 1 - Anomaly Detection:**
- Implemented a sliding window validation system with configurable preamble size
- Utilized the classic two-sum algorithm with hash set lookup for O(n) time complexity per validation
- Efficiently scanned the sequence to identify the first invalid number

**Part 2 - Contiguous Sum Search:**
- Applied a two-pointer sliding window technique to find contiguous subarrays
- Dynamically adjusted window size by expanding/contracting based on running sum
- Optimized to O(n) time complexity by maintaining a running total and single pass through data

## Technical Highlights

- **Hash-based lookups** for constant-time complement detection in the two-sum problem
- **Sliding window pattern** applied in two different contexts (fixed-size validation window and variable-size sum window)
- **Early termination** strategies to avoid unnecessary computation
- **Type hints and clean code structure** for maintainability and readability

## Example

```
Input: [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, ...]
Preamble size: 5

Part 1: Find first invalid number (e.g., 127 - not a sum of any two in previous 5)
Part 2: Find contiguous set summing to 127 (e.g., [15, 25, 47, 40]) → min + max = 62
```

## Key Takeaways

- Recognizing classic algorithmic patterns (two-sum, sliding window) in novel problem contexts
- Importance of window-based techniques for sequence analysis problems
- Clean separation of concerns with modular, reusable functions (`find_two_sum`, `part1`, `part2`)
  
## Usage

```bash
python solution.py
```