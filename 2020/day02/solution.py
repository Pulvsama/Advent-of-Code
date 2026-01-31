from typing import List, Tuple, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[Tuple[int, int], str, str]]:
    """Returns a list of tuples that are in the format ((n1, n2), "letter", "password")"""
    entries = []
    with open(filepath) as f:
        for line in f:
            bounds, letter_part, password = line.strip().split()
            n1, n2 = map(int, bounds.split("-"))
            letter = letter_part[0]
            entries.append(((n1, n2), letter, password))
    return entries

def check_password_part_1(entries: List[Tuple[Tuple[int, int], str, str]]) -> int:
    """Returns the number of correct codes according to the password policy of part 1"""
    valid = 0
    for (low, high), letter, password in entries:
        if low <= password.count(letter) <= high:
            valid += 1
    return valid

def check_password_part_2(entries: List[Tuple[Tuple[int, int], str, str]]) -> int:
    """Returns the number of correct codes according to the password policy of part 2"""
    valid = 0
    for (p1, p2), letter, password in entries:
        if (password[p1 - 1] == letter) != (password[p2 - 1] == letter): # Logical XOR
            valid += 1
    return valid

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", check_password_part_1(entries))
    print("Answer for part 2:", check_password_part_2(entries))