from typing import List, Optional, Tuple, Union
from pathlib import Path
import random
import time

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = SCRIPT_DIR / "input.txt"
TARGET_SUM = 2020

def load_numbers(filepath: Union[str, Path]) -> List[int]:
    """Reads whitespace-separated integers from a file."""
    with open(filepath) as f:
        return [int(x) for x in f.read().split()]
    
def generate_test_case(length: int, target: int) -> List[int]:
    """
    Generates a list of random integers. 
    Guarantees that at least one pair sums up to the target.
    """
    if length < 2:
        raise ValueError("List length must be at least 2")
    
    numbers = [random.randint(0, target * 2) for _ in range(length - 2)]
    n1 = random.randint(0, target)
    n2 = target - n1
    numbers.extend([n1, n2])
    random.shuffle(numbers)
    return numbers

def find_two_sum_set(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target."""
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None

def find_two_sum_brute_force(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target. 
    Using brute force, the complexity will be in O(n^2)"""
    n = len(numbers)
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None

if __name__ == "__main__":
    for length in 