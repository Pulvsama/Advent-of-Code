from typing import List, Union, Tuple, Optional
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[int]:
    """Returns a list of int corresponding to the numbers of the list"""
    with open(filepath) as f:
        return [int(x) for x in f.read().splitlines()]

def part1(entries: List[int]) -> int:
    """Returns the product of differences of 1 and 3 jolts"""
    adapters = sorted(entries)
    adapters = [0] + adapters + [adapters[-1] + 3]
    one_diff = 0
    three_diff = 0
    for a, b in zip(adapters, adapters[1:]):
        if b - a == 1:
            one_diff += 1
        elif b - a == 3:
            three_diff += 1

    return one_diff * three_diff

def part2(entries: List[int]) -> int:
    """Returns the number of distinct valid arrangements"""
    adapters = sorted(entries)
    adapters = [0] + adapters + [adapters[-1] + 3]
    ways = {0: 1}
    for a in adapters[1:]:
        ways[a] = (
            ways.get(a - 1, 0)
            + ways.get(a - 2, 0)
            + ways.get(a - 3, 0)
        )
    return ways[adapters[-1]]

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))