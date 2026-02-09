from typing import List, Union
from pathlib import Path
import copy

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """Returns a list of strings corresponding to the initial grid of seats"""
    with open(filepath) as f:
        return f.read().splitlines()

def part1(entries: List[str]) -> int:
    """Returns the number of occupied seats after the pattern converges (we assume it converges)"""
    grid = [list(row) for row in entries]
    while True:
        new_grid = copy.deepcopy(grid)
        for i, row in enumerate(grid):
            for j, seat in enumerate(row):
                if seat == "L":
                    occupied = sum(
                        1
                        for x in range(max(0, i - 1), min(len(grid), i + 2))
                        for y in range(max(0, j - 1), min(len(row), j + 2))
                        if (x, y) != (i, j) and grid[x][y] == "#"
                    )
                    if occupied == 0:
                        new_grid[i][j] = "#"
                elif seat == "#":
                    occupied = sum(
                        1
                        for x in range(max(0, i - 1), min(len(grid), i + 2))
                        for y in range(max(0, j - 1), min(len(row), j + 2))
                        if (x, y) != (i, j) and grid[x][y] == "#"
                    )
                    if occupied >= 4:
                        new_grid[i][j] = "L"
        if new_grid == grid:
            break
        grid = new_grid
    return sum(row.count("#") for row in grid)

def part2(entries: List[str]) -> int:
    """Returns the number of occupied seats after the pattern converges with the new visibility rules (we assume it converges)"""
    grid = [list(row) for row in entries]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while True:
        new_grid = copy.deepcopy(grid)
        for i, row in enumerate(grid):
            for j, seat in enumerate(row):
                if seat == "L":
                    occupied = 0
                    for di, dj in directions:
                        x, y = i + di, j + dj
                        while 0 <= x < len(grid) and 0 <= y < len(row):
                            if grid[x][y] == "#":
                                occupied += 1
                                break
                            elif grid[x][y] == "L":
                                break
                            x += di
                            y += dj
                    if occupied == 0:
                        new_grid[i][j] = "#"
                elif seat == "#":
                    occupied = 0
                    for di, dj in directions:
                        x, y = i + di, j + dj
                        while 0 <= x < len(grid) and 0 <= y < len(row):
                            if grid[x][y] == "#":
                                occupied += 1
                                break
                            elif grid[x][y] == "L":
                                break
                            x += di
                            y += dj
                    if occupied >= 5:
                        new_grid[i][j] = "L"
        if new_grid == grid:
            break
        grid = new_grid
    return sum(row.count("#") for row in grid)

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))