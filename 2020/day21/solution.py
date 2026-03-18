from typing import Union, List, Tuple, Optional
from pathlib import Path
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Tuple[List[str], List[str]]:
    """Returns the lists of foods and their according allergen list"""
    output = []
    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            foods, allergens = line.split("(contains ")
            foods = foods.split()
            for d in ",)":
                allergens = allergens.replace(d, "")
            allergens = allergens.split()
            output.append((foods, allergens))
    return output # pyright: ignore[reportReturnType]

def part1(entries: Tuple[List[str], List[str]]) -> int:
    """Returns the number of elements that contain no allergen"""
    d = defaultdict(set)
    for foods, allergens in entries:
        for allergen in allergens:
            if allergen in d:
                d[allergen] &= set(foods)
                if not d[allergen]:
                    raise ValueError("allergen in imaginary food")
            else:
                d[allergen] = set(foods)
    contains_allergen = set()
    while d:
        progress = False
        for allergen, possible_food in list(d.items()):
            if len(possible_food) == 1:
                food = next(iter(possible_food))
                del d[allergen]
                for other in d.values():
                    other.discard(food)
                contains_allergen.add(food)
                progress = True
        if not progress:
            raise ValueError("No progress, something wrong")
    count = 0
    for line in entries:
        foods, _ = line
        for food in foods:
            if food not in contains_allergen:
                count += 1
    return count

def part2(entries: Tuple[List[str], List[str]]) -> str:
    """Returns the list of foods containing allergens sorted alphabetically by their according allergens"""
    d = defaultdict(set)
    for foods, allergens in entries:
        for allergen in allergens:
            if allergen in d:
                d[allergen] &= set(foods)
                if not d[allergen]:
                    raise ValueError("allergen in imaginary food")
            else:
                d[allergen] = set(foods)
    contains_allergen = {}
    while d:
        progress = False
        for allergen, possible_food in list(d.items()):
            if len(possible_food) == 1:
                food = next(iter(possible_food))
                del d[allergen]
                for other in d.values():
                    other.discard(food)
                contains_allergen[food] = allergen
                progress = True
        if not progress:
            raise ValueError("No progress, something wrong")
    foods_with_allergen = [food for food, allergen in sorted(contains_allergen.items(), key=lambda x : x[1])]
    return ",".join(foods_with_allergen)

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1: ", part1(entries))
    print("Answer for part 2: ", part2(entries))