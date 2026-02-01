from typing import List, Tuple, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """From the input.txt, returns the entire forest as a list of strings"""
    with open(filepath) as f:
        return [x for x in f.read().splitlines()]
    
def count_trees(forest: List[str]) -> int:
    """Counts the number of trees encountered when going in a straight line 
    with a slope of 3 to the righyt and 1 down and returns that number"""
    tree_count = 0

    # Since we start at the top and go down 1 each time, we loop over the height of the forest
    height = len(forest)
    width = len(forest[0])      # Width of one forest
    for i in range(height):
        # We're not going to copy the forest until we have "enough" but rather work cyclically
        j = (3 * i) % width
        if forest[i][j] == '#':
            tree_count += 1
    return tree_count

def count_trees_slope(slopes: List[Tuple[int, int]], forest: List[str]) -> int:
    """Counts the number of trees encountered when going in a straight line with slopes of:
    1 right, 1 down, 
    3 right, 1 down,
    5 right, 1 down,
    7 right, 1 down,
    1 right, 2 down
    Returns the resulting number when mulplying all these numbers."""
    result = 1
    for x, y in slopes:
        tree_count = 0
        height, width = len(forest), len(forest[0])
        for i in range(0, height, y):
            j = (x * i//y) % width
            if forest[i][j] == '#':
                tree_count += 1
        result *= tree_count
    return result


if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", count_trees(entries))
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    print("Answer for part 2:", count_trees_slope(slopes, entries))