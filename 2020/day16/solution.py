from typing import List, Union
from pathlib import Path
import bisect

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[List[str]]:
    """Returns the rules, my ticket and the nearby tickets"""
    with open(filepath) as f:
        rules, ticket, nearby = f.read().strip().split("\n\n")
        return [rules.splitlines(), ticket.splitlines(), nearby.splitlines()]

def merge_intervals(bounds: List[List[int]]) -> List[List[int]]:
    """Merges and sorts the bounds"""
    bounds.sort()
    merged = []
    for l, r in bounds:
        if not merged or merged[-1][1] < l:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)
    return merged 

def part1(entries: List[List[str]]) -> int:
    """Returns the scanning error rate"""
    rules, _, nearby = entries
    all_bounds = []
    result = []
    for rule in rules:
        _, bounds = rule.split(": ")
        bounds = bounds.split(" or ")
        for bound in bounds:
            lower, upper = bound.split("-")
            all_bounds.append([int(lower), int(upper)])
    all_bounds = merge_intervals(all_bounds)
    left_bounds = [l for l,_ in all_bounds]
    for ticket in nearby[1:]:
        numbers = [int(number) for number in ticket.split(",")]
        for number in numbers:
            i = bisect.bisect_right(left_bounds, number) - 1
            if i < 0 or number > all_bounds[i][1]:
                result.append(number)
    return sum(result)

def part2(entries: List[List[str]]) -> int:
    """Returns a dictionary where the keys are the names of the class and the values theirs index"""
    rules, my_ticket, nearby = entries
    all_bounds = []
    cleaned_numbers = []
    list_of_bounds = []
    for rule in rules:
        name, bounds = rule.split(": ")
        bounds = bounds.split(" or ")
        both = []
        for bound in bounds:
            lower, upper = bound.split("-")
            all_bounds.append([int(lower), int(upper)])
            both.append([int(lower), int(upper)])
        list_of_bounds.append((name, both))
    all_bounds = merge_intervals(all_bounds)
    left_bounds = [l for l,_ in all_bounds]
    for ticket in nearby[1:]:
        numbers = [int(n) for n in ticket.split(",")]
        valid = True
        for number in numbers:
            i = bisect.bisect_right(left_bounds, number) - 1
            if i < 0 or number > all_bounds[i][1]:
                valid = False
                break
        if valid:
            cleaned_numbers.append(numbers)
    columns = list(zip(*cleaned_numbers))
    possible = {i: [] for i in range(len(columns))}
    for i, column in enumerate(columns):
        for name, bounds in list_of_bounds:
            valid = True
            for number in column:
                if not (
                    bounds[0][0] <= number <= bounds[0][1]
                    or bounds[1][0] <= number <= bounds[1][1]
                ):
                    valid = False
                    break
            if valid:
                possible[i].append(name)
    correct_names = {}
    possible = {i: set(possible_names) for i, possible_names in possible.items()}
    while len(correct_names) < len(columns):
        progress = False
        for i, names in possible.items():
            if len(names) == 1:
                name = next(iter(names))
                correct_names[name] = i
                del possible[i]
                for other in possible.values():
                    other.discard(name)
                progress = True
                break
        if not progress:
            raise RuntimeError("Cannot resolve further")
    result = 1
    my_values = [int(x) for x in my_ticket[1].split(",")]
    for name, index in correct_names.items():
        if name.startswith("departure"):
            result *= my_values[index]
    return result

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1", part1(entries))
    print("Answer for part 2", part2(entries))