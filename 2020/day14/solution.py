from typing import List, Union
from pathlib import Path
from itertools import product

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    with open(filepath, "r") as f:
        return f.read().splitlines()

def part1(entries: List[str]) -> int:
    """Returns the sum of all values left in memory after processing the initialization program."""
    mask = None
    memory = {}
    for entry in entries:
        if entry.startswith("mask"):
            mask = entry.split(" = ")[1]
        else:
            mem_loc, value = entry.split(" = ")
            mem_loc = int(mem_loc[4:-1])
            value = int(value)
            and_mask = int(mask.replace("X", "1"), 2)   # pyright: ignore[reportOptionalMemberAccess]
            or_mask = int(mask.replace("X", "0"), 2)    # pyright: ignore[reportOptionalMemberAccess]
            memory[mem_loc] = (value & and_mask) | or_mask
    return sum(memory.values())

def fill_x(template: str, bits: str) -> str:
    """Replaces all the Xs by the template provided"""
    bits_iter = iter(bits)
    return "".join(next(bits_iter) if c == "X" else c for c in template)

def part2(input_data: List[str]) -> int:
    mask = None
    memory = {}
    for entry in input_data:
        if entry.startswith("mask"):
            mask = entry.split(" = ")[1]
        else:
            mem_loc, value = entry.split(" = ")
            address = format(int(mem_loc[4:-1]), "036b")
            value = int(value)
            after_mask = ""
            X_number = 0
            for i in range(len(mask)):      # pyright: ignore[reportArgumentType]
                if mask[i] == "0":          # pyright: ignore[reportOptionalSubscript]
                    after_mask += address[i]
                elif mask[i] == "1":        # pyright: ignore[reportOptionalSubscript]
                    after_mask += "1"
                else:
                    after_mask += "X"
                    X_number += 1
            for bits in product("01", repeat=X_number):
                sequence = "".join(bits)
                new_address = int(fill_x(after_mask, sequence), 2)
                memory[new_address] = value
    return sum(memory.values())

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Part 1:", part1(entries))
    print("Part 2:", part2(entries))