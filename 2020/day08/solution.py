from typing import List, Union, Tuple
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[str, str]]:
    """Returns a list of instructions (operation, argument)."""
    with open(filepath) as f:
        return [tuple(line.strip().split()) for line in f] # pyright: ignore[reportReturnType]

    
def run(instructions: List[Tuple[str, str]]) -> Tuple[int, bool]:
    """
    Executes the program.
    Returns (accumulator, terminated_normally).
    """
    visited = set()
    acc = 0
    i = 0
    n = len(instructions)
    while i < n:
        if i in visited:
            return acc, False
        visited.add(i)
        op, arg = instructions[i]
        if op == "acc":
            acc += int(arg)
        elif op == "jmp":
            i += int(arg)
            continue
        i += 1

    return acc, True


def part1(entries: List[Tuple[str, str]]) -> int:
    """Returns the accumulator value right before an instruction is executed twice."""
    acc, _ = run(entries)
    return acc


def part2(entries: List[Tuple[str, str]]) -> int:
    """Returns the accumulator value after fixing the program."""
    for i, (op, arg) in enumerate(entries):
        if op not in ("jmp", "nop"):
            continue
        modified = entries.copy()
        modified[i] = ("nop" if op == "jmp" else "jmp", arg)
        acc, terminated = run(modified)
        if terminated:
            return acc
    raise ValueError("No solution found")


if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))