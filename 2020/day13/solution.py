from typing import List, Union, Tuple
from pathlib import Path
import math

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Tuple[int, List[str]]:
    """Returns a tuple where the first element is the earliest timestamp and the second is the list of bus IDs"""
    with open(filepath) as f:
        x = f.read().splitlines()
        return (int(x[0]), x[1].split(","))

def part1(entries: Tuple[int, List[str]]) -> int:
    """Returns the product of the minutes we have to wait by the ID of the earliest bus we can take"""
    min_wait = 10**18
    min_id = -1
    timestamp = int(entries[0])
    for bus in entries[1]:
        if bus.isdigit():
            bus_id = int(bus)
            wait = (-timestamp) % bus_id
            if wait < min_wait:
                min_wait = wait
                min_id = bus_id
    return min_id * min_wait

def part2(entries: Tuple[int, List[str]]) -> int:
    """Returns the timestamp where the first occurence of the phenomena described appears"""
    t = 0
    step = 1
    for i in range(len(entries[1])):
        bus = entries[1][i]
        offset = i
        if bus.isdigit():
            bus_id = int(bus)
            while (t + offset) % bus_id != 0:
                t += step
            step *= bus_id
    return t

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))
    