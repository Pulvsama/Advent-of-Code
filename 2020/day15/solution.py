from typing import List, Union
from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[int]:
    """Returns the list of the first numbers"""
    with open(filepath) as f:
        return [int(x) for x in f.read().split(",")]

def part1(entries: List[int]) -> int:
    """Returns the 2020th number of the elves' game"""
    memory = {}
    idx = 1
    for x in entries:
        memory[x] = idx
        idx += 1
        last_value = x
    while idx <= 2020:
        if last_value in memory:
            old_idx = memory[last_value]
            memory[last_value] = idx - 1
            last_value = idx - 1 - old_idx
        else:
            memory[last_value] = idx - 1
            last_value = 0
        idx +=1
    return last_value

def part2(entries: List[int]) -> int:
    """Returns the 30000000th number of the elves' game"""
    memory = {}
    idx = 1
    for x in entries:
        memory[x] = idx
        idx += 1
        last_value = x
    while idx <= 30000000:
        if last_value in memory:
            old_idx = memory[last_value]
            memory[last_value] = idx - 1
            last_value = idx - 1 - old_idx
        else:
            memory[last_value] = idx - 1
            last_value = 0
        idx +=1
    return last_value

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    start_time = time.perf_counter()
    print("Answer for part 2:", part2(entries))
    end_time = time.perf_counter()
    print(end_time - start_time)