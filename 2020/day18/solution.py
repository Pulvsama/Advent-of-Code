from typing import Union, List, Set, Tuple
from pathlib import Path
from collections import deque
import operator

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """Returns the list of math operations"""
    with open(filepath) as f:
        return f.read().splitlines()

def evaluate(expression: str) -> int:
    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
    pos = 0

    def parse():
        nonlocal pos
        left = None
        op = None
        while pos < len(tokens):
            token = tokens[pos]
            pos += 1

            if token == ")":
                break
            
            if token == "(":
                value = parse()
            elif token in ("+", "*"):
                op = token
                continue
            else:
                value = int(token)

            if left is None:
                left = value
            else:
                if op == "+":
                    left += value # pyright: ignore[reportOperatorIssue]
                elif op == "*":
                    left *= value # pyright: ignore[reportOperatorIssue]

        return left

    return parse() # pyright: ignore[reportReturnType]

def part1(entries: List[str]) -> int:
    """Returns the sum of all the operations"""
    result = 0
    for expression in entries:
        result += evaluate(expression)
    return result

def evaluate_prec(expression: str) -> int:
    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
    pos = 0

    precedence = {
        "+": 2,
        "*": 1
    }

    def parse_atom() -> int:
        nonlocal pos
        token = tokens[pos]
        pos += 1
        if token == "(":
            value = parse(0)
            pos += 1
            return value
        return int(token)

    def parse(min_prec: int = 0) -> int:
        nonlocal pos
        left = parse_atom()

        while pos < len(tokens):
            op = tokens[pos]
            if op == ")" or op not in precedence:
                break

            prec = precedence[op]
            if prec < min_prec:
                break

            pos += 1
            right = parse(prec + 1)

            if op == "+":
                left += right
            else:
                left *= right

        return left

    return parse(0)



def part2(entries: List[str]) -> int:
    """Returns the sum of all the operations with precedence"""
    result = 0
    for expression in entries:
        result += evaluate_prec(expression)
    return result

if __name__ == "__main__":
    entries = load_input(TEST_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))