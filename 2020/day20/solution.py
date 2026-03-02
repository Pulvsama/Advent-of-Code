from typing import Union, List, Tuple, Dict, Pattern
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[int, List[str]]]:
    """Returns the list of tiles as a list of tuples (tile_number, tile)"""
    tiles = []
    with open(filepath) as f:
        for tile in f.read().split('\n\n'):
            tile_number, image = tile.split(':\n')
            tile_number = tile_number[5:]
            image = image.split()
            tiles.append((tile_number, image))
    return tiles

if __name__ == "__main__":
    entries = load_input(TEST_FILE)
    print(format(2, "004b") + format(4, "004b"))