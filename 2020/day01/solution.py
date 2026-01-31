from typing import List, Optional, Tuple, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

INPUT_FILE = SCRIPT_DIR / "input.txt"
TARGET_SUM = 2020

def load_numbers(filepath: Union[str, Path]) -> List[int]:
    """Reads whitespace-separated integers from a file."""
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

if __name__ == "__main__":
    numbers = load_numbers(INPUT_FILE)
    pair = find_two_sum(TARGET_SUM, numbers)
    if pair:
        n1, n2 = pair
        print("Answer:", n1 * n2)