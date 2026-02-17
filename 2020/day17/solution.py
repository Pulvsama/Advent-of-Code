from typing import Union, Set, Tuple
from pathlib import Path
from itertools import product
import copy

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Set[Tuple[int, int, int]]:
    """Returns the states of the initial flat surface"""
    with open(filepath) as f:
        active = set()
        grid = f.read().splitlines()
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[x][y] == "#":
                    active.add((x, y, 0))
    return active

def part1(entries: Set[Tuple[int, int, int]]) -> int:
    """Returns the amount of active cubes after the six cycles"""
    state = entries
    for _ in range(6):
        neighbors = list(product([-1, 0, 1], repeat=3))
        neighbors.remove((0, 0, 0))
        to_check = set()
        next_state = set()
        for cube in state:
            x, y, z = cube
            to_check.add((x, y, z))
            for dx, dy, dz in neighbors:
                to_check.add((x + dx, y + dy, z + dz))
        for cube in to_check:
            x, y, z = cube
            count = sum(1 if (x + dx, y + dy, z + dz) in state else 0 for (dx, dy, dz) in neighbors)
            if count in (2,3) and cube in state:
                next_state.add(cube)
            if count == 3 and cube not in state:
                next_state.add(cube)
        state = copy.deepcopy(next_state)
    return len(state)

def part2(entries: Set[Tuple[int, int, int]]) -> int:
    """Returns the amount of active cubes after six cycles in the 4D case"""
    state = set()
    for cube in entries:
        x, y, z = cube
        state.add((x, y, z, 0))
    for _ in range(6):
        neighbors = list(product([-1, 0, 1], repeat=4))
        neighbors.remove((0, 0, 0, 0))
        to_check = set()
        next_state = set()
        for cube in state:
            x, y, z, w = cube
            to_check.add((x, y, z, w))
            for dx, dy, dz, dw in neighbors:
                to_check.add((x + dx, y + dy, z + dz, w + dw))
        for cube in to_check:
            x, y, z, w = cube
            count = sum(1 if (x + dx, y + dy, z + dz, w + dw) in state else 0 for (dx, dy, dz, dw) in neighbors)
            if count in (2,3) and cube in state:
                next_state.add(cube)
            if count == 3 and cube not in state:
                next_state.add(cube)
        state = copy.deepcopy(next_state)
    return len(state)

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))