from typing import List, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """Returns a list of strings corresponding to the boarding passes"""
    with open(filepath) as f:
        return f.read().splitlines()
    
def highest_seat_id(entries: List[str]) -> int:
    """From the boarding passes list, returns the highest seat ID"""
    highest = 0
    for seat in entries:
        row_bit = seat[:7].replace("F", "0").replace("B", "1")
        row = int(row_bit, 2)
        column_bit = seat[7:].replace("L", "0").replace("R", "1")
        column = int(column_bit, 2)
        highest = max(highest, 8 * row + column)
    return highest

def what_is_my_seat(entries: List[str]) -> int:
    """Returns our seat ID"""
    passengers = []
    for seat in entries:
        row_bit = seat[:7].replace("F", "0").replace("B", "1")
        row = int(row_bit, 2)
        column_bit = seat[7:].replace("L", "0").replace("R", "1")
        column = int(column_bit, 2)
        passengers.append(8 * row + column)
    passengers = sorted(passengers)
    for i in range(len(passengers) - 1):
        if passengers[i + 1] != passengers[i] + 1:
            return passengers[i] + 1
    return -1

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", highest_seat_id(entries))
    print("Answer for part 2:", what_is_my_seat(entries))