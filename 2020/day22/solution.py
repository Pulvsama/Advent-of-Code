from typing import Union, List, Tuple, Deque, Set
from pathlib import Path
from collections import deque
from itertools import islice

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> Tuple[List[int], List[int]]:
    """Returns both players decks"""
    with open(filepath) as f:
        p1, p2 = f.read().split("\n\n")
        p1, p2 = p1.split(), p2.split()
        deck1, deck2 = [], []
        for x1, x2 in zip(p1[2:], p2[2:]):
            deck1.append(int(x1))
            deck2.append(int(x2))
    return deck1, deck2

def calculate_score(deck: List[int]) -> int:
    return sum((i+1) * x for i, x in enumerate(deck[::-1]))

def part1(entries: Tuple[List[int], List[int]]) -> int:
    """Returns the score of the winner"""
    deck1, deck2 = deque(entries[0]), deque(entries[1])
    while deck1 and deck2:
        x1, x2 = deck1.popleft(), deck2.popleft()
        if x1 > x2:
            deck1.append(x1)
            deck1.append(x2)
        elif x1 < x2:
            deck2.append(x2)
            deck2.append(x1)
        else:
            raise ValueError(x1, x2, "Tie, can't handle it")

    if deck1:
        return calculate_score(list(deck1))
    else:
        return calculate_score(list(deck2))

def part2(entries: Tuple[List[int], List[int]]) -> int:
    """Returns the score of the winner with subgames and without infinite loops"""
    def subgame(deck1: Deque[int], deck2: Deque[int], memory: Set[Tuple[Tuple[int,...], Tuple[int,...]]]) -> bool:
        """Returns True if P1 wins and False otherwise. If needed, plays the subgame by calling itself recursively. No infinite game possible"""
        while deck1 and deck2:
            state = (tuple(deck1), tuple(deck2))
            if state in memory:
                return True
            else:
                memory.add(state)
                x1, x2 = deck1.popleft(), deck2.popleft()
                n1, n2 = len(deck1), len(deck2)
                if x1 <= n1 and x2 <= n2:
                    subdeck1, subdeck2 = deque(islice(deck1, 0, x1)), deque(islice(deck2, 0, x2))
                    p1_won = subgame(subdeck1, subdeck2, set())
                    if p1_won:
                        deck1.append(x1)
                        deck1.append(x2)
                    else:
                        deck2.append(x2)
                        deck2.append(x1)
                else:
                    if x1 > x2:
                        deck1.append(x1)
                        deck1.append(x2)
                    elif x1 < x2:
                        deck2.append(x2)
                        deck2.append(x1)
                    else:
                        raise ValueError(x1, x2, "Tie, can't handle it")
        if deck1:
            return True
        else:
            return False
    deck1, deck2 = deque(entries[0]), deque(entries[1])
    p1_won = subgame(deck1, deck2, set())
    if p1_won:
        return calculate_score(list(deck1))
    else:
        return calculate_score(list(deck2))

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries))
    print("Answer for part 2:", part2(entries))