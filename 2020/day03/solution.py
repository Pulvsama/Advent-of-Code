from typing import List, Tuple, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """From the input.txt, returns the entire forest as a list of strings"""
    with open(filepath) as f:
        return [x for x in f.read().splitlines()]

if __name__ == "__main__":
    