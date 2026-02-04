from typing import List, Union, Tuple, Dict
from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Tuple[Dict[str, List[str]], Dict[str, List[Tuple[str, int]]]]:
    """Returns two adjacency dictionaries:
    - contained_by: inner_color -> [outer_colors] (for Part 1: what bags can hold this color)
    - contains: outer_color -> [(inner_color, count)] (for Part 2: what this bag contains)
    Changed after discovering part 2
    """
    with open(filepath) as f:
        lines = f.read().strip().splitlines()
    contains = {}
    contained_by = {}
    for line in lines:
        outer, inner = line.split(" bags contain ")
        if inner == "no other bags.":
            contains[outer] = []
        else:
            seps = sorted(["bag", "bags", "bag,", "bags,", "bag.", "bags."], key=len, reverse=True)
            inner_colors = [color.strip() for color in re.split('|'.join(map(re.escape, seps)), inner) if color]
            for inner_color in inner_colors:
                number, color = inner_color.split(" ", 1)
                if outer in contains:
                    contains[outer].append((color, int(number)))
                else:
                    contains[outer] = [(color, int(number))]
                if color in contained_by:
                    contained_by[color].append(outer)
                else:
                    contained_by[color] = [outer]
    return contained_by, contains

def part1(rules: Dict[str, List[str]]) -> int:
    """Returns the number of bags that can contain the shiny gold bag according to the rules"""
    can_contain = rules["shiny gold"]
    possible_bags = set()
    while can_contain:
        bag = can_contain.pop()
        if bag not in possible_bags:
            possible_bags.add(bag)
            if bag in rules:
                can_contain.extend(rules[bag])
    return len(possible_bags)

def part2(rules: Dict[str, List[Tuple[str, int]]]) -> int:
    """Returns the number of bags the shiny gold bag must contain according to the rules"""
    def dfs(bag: str) -> int:
        """Does a Depth First Search to count the number of bags a specific bag must contain according to the rules"""
        total = 0
        for inner_bag, count in rules.get(bag, []):
            total += count * (1 + dfs(inner_bag))
        return total
    return dfs("shiny gold")

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries[0]))
    print("Answer for part 2:", part2(entries[1]))