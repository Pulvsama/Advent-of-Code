from typing import List, Union, Tuple
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[str,...]]:
    """Returns a list of tuples in the form (operation, argument)"""
    with open(filepath) as f:
        return [tuple(x.strip().split()) for x in f.read().splitlines()]
    
def part1(instructions: List[Tuple[str, str]]) -> int:
    """Returns the """

if __name__ == "__main__":
    print(load_input(TEST_FILE))