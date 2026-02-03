from typing import List, Union, Dict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Dict[str, str]]:
    """Returns a list of dictionaries corresponding to the input"""
    entries = []
    with open(filepath) as f:
        blocks = f.read().strip().split("\n\n")
        for block in blocks:
            split = block.replace(":", " ").split()
            d = dict(zip(split[::2], split[1::2]))
            entries.append(d)
    return entries

def count_valid_passports(entries: List[Dict[str, str]]) -> int:
    """Returns the number of valid passports according to our new rule"""
    valid = 0
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in entries:
        if all(field in passport for field in expected_fields):
            valid += 1
    return valid

# Functions to validate the fields
def is_valid_byr(byr: str) -> bool:
    return byr.isdigit() and 1920 <= int(byr) <= 2002

def is_valid_iyr(iyr: str) -> bool:
    return iyr.isdigit() and 2010 <= int(iyr) <= 2020

def is_valid_eyr(eyr: str) -> bool:
    return eyr.isdigit() and 2020 <= int(eyr) <= 2030

def is_valid_hgt(hgt: str) -> bool:
    if hgt.endswith("cm"):
        return hgt[:-2].isdigit() and 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith("in"):
        return hgt[:-2].isdigit() and 59 <= int(hgt[:-2]) <= 76
    else:
        return False
    
def is_valid_hcl(hcl: str) -> bool:
    return len(hcl) == 7 and hcl[0] == "#" and all(c in "abcdef0123456789" for c in hcl[1:])

def is_valid_ecl(ecl: str) -> bool:
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_valid_pid(pid: str) -> bool:
    return pid.isdigit() and len(pid) == 9

def count_valid_passports_and_values(entries: List[Dict[str, str]]) -> int:
    """Returns the number of valid passports according to our new rule AND with valid values"""
    valid = 0
    validators = {
        "byr": is_valid_byr,
        "iyr": is_valid_iyr,
        "eyr": is_valid_eyr,
        "hgt": is_valid_hgt,
        "hcl": is_valid_hcl,
        "ecl": is_valid_ecl,
        "pid": is_valid_pid
    }
    for passport in entries:
        if all(field in passport and validator(passport[field]) for field, validator in validators.items()):
            valid += 1
    return valid

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", count_valid_passports(entries))
    print("Answer for part 2:", count_valid_passports_and_values(entries))