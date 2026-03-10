from typing import Union, List
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[int]:
    """Returns the initial ordering."""
    with open(filepath) as f:
        return [int(x) for x in f.read()]
    
def part1(entries: List[int]) -> int:
    """Returns the order after the cup 1 after 100 moves"""
    move = 1
    next_cup = [0] * (len(entries) + 1)
    for i in range(len(entries)):
        next_cup[entries[i-1]] = entries[i]
    current = entries[0]
    while move <= 100:
        a = next_cup[current]
        b = next_cup[a]
        c = next_cup[b]
        next_c = next_cup[c]
        next_cup[current] = next_c
        destination = current - 1 or 9
        while destination in (a, b, c):
            destination = destination - 1 or 9
        next_cup[c] = next_cup[destination]
        next_cup[destination] = a
        current = next_cup[current]
        move += 1
    current = 1
    final = 0
    for _ in range(8):
        current = next_cup[current]
        final = 10* final + current
    return final

def part2(entries: List[int]) -> int:
    """Returns the result of the multiplication of the two cups right next to 1 after the simulation"""
    move = 1
    cups = [num for num in entries]
    for i in range(10, 1000001):
        cups.append(i)
    next_cup = [0] * 1000001
    for i in range(1000000):
        next_cup[cups[i-1]] = cups[i]
    current = cups[0]
    while move <= 10000000:
        a = next_cup[current]
        b = next_cup[a]
        c = next_cup[b]
        next_c = next_cup[c]
        next_cup[current] = next_c
        destination = current - 1 or 1000000
        while destination in (a, b, c):
            destination = destination - 1 or 1000000
        next_cup[c] = next_cup[destination]
        next_cup[destination] = a
        current = next_cup[current]
        move += 1
    return next_cup[1] * next_cup[next_cup[1]]

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))