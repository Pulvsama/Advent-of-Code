from typing import List, Union, Tuple, Optional
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[int]:
    """Returns a list of int corresponding to the numbers of the list"""
    with open(filepath) as f:
        return [int(x) for x in f.read().splitlines()]

def find_two_sum(target: int, numbers: List[int]) -> Optional[Tuple[int, int]]:
    """Finds a pair of numbers that sum to the target."""
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None

def part1(k: int, nums: List[int]) -> Optional[Tuple[int, int]]:
    """Returns the first number of nums that isn't a sum of two of the previous k numbers"""
    assert k > 1, "k is too small"
    for i in range(k, len(nums)):
        if not find_two_sum(nums[i], nums[i-k:i]):
            return nums[i], i
    return None
    
def part2(target: int, nums: List[int]) -> Optional[int]:
    """Finds a contiguous subarray of nums such that the elements sum up to target, 
    Returns the sum of the min and max of this subarray"""
    l = 0
    total = 0
    for r in range(len(nums)):
        total += nums[r]
        while total > target:
            total -= nums[l]
            l += 1
        if total == target and r > l:
            window = nums[l:r+1]
            return min(window) + max(window)
    return None

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(25, entries))
    print("Answer for part 2:", part2(70639851, entries))