from typing import List, Union, Tuple
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[str, int]]:
    """Returns the list of actions as a list of tuples (str, int)"""
    with open(filepath) as f:
        return [(x[0], int(x[1:])) for x in f.read().splitlines()]
    
def part1(entries: List[Tuple[str, int]]) -> int:
    """Returns the Manhattan distance of the destination after the instructions"""
    east = north = 0
    directions = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
    direction = 'E'
    for instruction in entries:
        action = instruction[0]
        value = instruction[1]
        if action == 'F':
            dx, dy = directions[direction]
            east += value * dx
            north += value * dy
        elif action == 'L':
            n = value // 90
            direction = 'NESW'[('NESW'.index(direction) - n)% 4]
        elif action == 'R':
            n = value // 90
            direction = 'NESW'[('NESW'.index(direction) + n)% 4]
        else:
            dx, dy = directions[action]
            east += value * dx
            north += value * dy
    return abs(east) + abs(north)

def part2(entries: List[Tuple[str, int]]) -> int:
    """Returns the Manhattan distance of the destination after the instructions with the new rules"""
    east = north = 0
    waypoint_east = 10
    waypoint_north = 1
    directions = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W': (-1,0)}
    for instruction in entries:
        action = instruction[0]
        value = instruction[1]
        if action == 'F':
            east += value * waypoint_east
            north += value * waypoint_north
        elif action == 'L':
            n = value // 90
            for _ in range(n):
                waypoint_east, waypoint_north = -waypoint_north, waypoint_east
        elif action == 'R':
            n = value // 90
            for _ in range(n):
                waypoint_east, waypoint_north = waypoint_north, -waypoint_east
        else:
            dx, dy = directions[action]
            waypoint_east += value * dx
            waypoint_north += value * dy
    return abs(east) + abs(north)

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))
