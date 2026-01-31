from typing import List, Optional, Tuple, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = SCRIPT_DIR / "input.txt"
TARGET_SUM = 2020

def load_numbers(filepath: Union[str, Path]) -> List[int]:
    """Loads numbers"""
    with open(filepath) as f:
        return [int(x) for x in f.read().split()]

def find_two_sum(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target."""
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None

def find_three_sum(target: int, numbers: List[int]) -> Optional[Tuple[int, int, int]]:
    """Finds a triplet of numbers that sum to the target"""
    for number in numbers:
        complement = target - number
        residual = numbers.copy()
        residual.remove(number)
        res_two_sum = find_two_sum(complement, residual)
        if res_two_sum:
            return (number, res_two_sum[0], res_two_sum[1])
    return None


if __name__ == "__main__":
    numbers = load_numbers(INPUT_FILE)
    
    "Part 1 solver"
    print("Solving two-sum")
    pair = find_two_sum(TARGET_SUM, numbers)
    if pair:
        n1, n2 = pair
        print("Answer:", n1 * n2)
    
    "Part 2 solver"
    print("Solving three-sum")
    triplet = find_three_sum(TARGET_SUM, numbers)
    if triplet:
        n1, n2, n3 = triplet
        print("Answer:", n1 * n2 * n3)