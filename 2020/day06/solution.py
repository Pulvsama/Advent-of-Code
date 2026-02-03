from typing import List, Union
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[List[str]]:
    """Returns a list of strings corresponding to the group's answers"""
    entries = []
    with open(filepath) as f:
        groups = f.read().strip().split("\n\n")
        for group in groups:
            answers = group.strip().split()
            entries.append(answers)
    return entries

def count_yes(entries: List[List[str]]) -> int:
    """Returns the sum of numbers of yes (does not count duplicates) in each group"""
    count = 0
    for group in entries:
        anwsers = "".join(group)
        count += len(set(anwsers))
    return count

def count_everyone_yes(entries: List[List[str]]) -> int:
    """Returns the sum of the numbers of questions where everyone in the group said yes"""
    count = 0
    for group in entries:
        common_yes = set.intersection(*map(set, group))
        count += len(common_yes)
    return count

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", count_yes(entries))
    print("Answer for part 2:", count_everyone_yes(entries))