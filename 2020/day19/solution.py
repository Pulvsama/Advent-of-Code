from typing import Union, List, Tuple, Dict, Pattern
from pathlib import Path
from collections import defaultdict
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Tuple[List[str], List[str]]:
    """Returns the rules and the messages to be checked"""
    with open(filepath) as f:
        rules, messages = f.read().strip().split("\n\n")
        return rules.splitlines(), messages.splitlines()

def build_regex(rules: Dict[int, List[List[str]]]) -> Pattern:
    """Returns a matcher from the rules"""
    cache = {}

    def build(n):
        if n in cache:
            return cache[n]

        rule = rules[n]

        if rule[0][0].isalpha():
            cache[n] = rule[0][0]
            return cache[n]

        parts = []

        for alternative in rule:
            subpattern = ""

            for token in alternative:
                subpattern += build(int(token))

            parts.append(subpattern)

        if len(parts) == 1:
            result = parts[0]
        else:
            result = "(" + "|".join(parts) + ")"

        cache[n] = result
        return result

    pattern = "^" + build(0) + "$"
    return re.compile(pattern)

def part1(entries: Tuple[List[str], List[str]]) -> int:
    """Returns the number of messages that matches the rule 0"""
    rules = defaultdict(list)
    messages = entries[1]
    for rule in entries[0]:
        num, matches = rule.split(": ")
        matches = matches.strip('"')
        rules[int(num)] = [match.split() for match in matches.split(" | ")]
    regex = build_regex(rules)

    return sum(bool(regex.match(m)) for m in messages)

def part2(entries: Tuple[List[str], List[str]]) -> int:
    """"""

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))