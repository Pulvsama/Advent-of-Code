from typing import Union, List, Tuple
from pathlib import Path
import copy
import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[str]:
    """Returns the lsit of directions"""
    with open(filepath) as f:
        return f.read().splitlines()

def read_line(line: str) -> Tuple[int, int]:
    """Returns the coordinates of the resulting tile in the hex-map coordinates system.
    I am putting the center of the hex-map at coordinate (0,0). 
    I will use the axial coordinate system for my hex map."""
    E, NE, NW, W, SW, SE  = (1,0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)
    directions = {"e": E, "ne": NE, "nw": NW, "w": W, "sw": SW, "se": SE}
    i = 0
    n = len(line)
    coord = (0,0)
    while i < n:
        dir = line[i]
        if dir in "ns":
            i += 1
            dir += line[i]
        q, r = coord
        dq, dr = directions[dir]
        coord = (q + dq, r + dr)
        i += 1
    return coord

def part1(entries: List[str]) -> int:
    """Returns the number of black tiles"""
    black = set()
    for line in entries:
        coord = read_line(line)
        if coord in black:
            black.remove(coord)
        else:
            black.add(coord)
    return len(black)

def plot_hexagons(*frames, radius=1, labels=None):
    """Plot one or more hex states. Use left/right arrow keys to switch between them."""
    if not frames:
        return
    if labels is None:
        labels = [f"State {i}" for i in range(len(frames))]

    fig, ax = plt.subplots()
    state = {"index": 0}

    def draw(idx):
        ax.clear()
        for q, r in frames[idx]:
            x = math.sqrt(3) * (q + r / 2)
            y = 1.5 * r
            hexagon = RegularPolygon(
                (x, y),
                numVertices=6,
                radius=radius,
            )
            ax.add_patch(hexagon)
            ax.text(x, y, f"{q},{r}", ha="center", va="center")
        ax.set_aspect("equal")
        ax.autoscale_view()
        ax.set_title(f"{labels[idx]}  ({idx + 1}/{len(frames)})")
        fig.canvas.draw_idle()

    def on_key(event):
        if event.key == "right" and state["index"] < len(frames) - 1:
            state["index"] += 1
            draw(state["index"])
        elif event.key == "left" and state["index"] > 0:
            state["index"] -= 1
            draw(state["index"])

    fig.canvas.mpl_connect("key_press_event", on_key)
    draw(0)
    plt.show()

def part2(entries: List[str]) -> int:
    """Returns the number of black tiles after 100 days."""
    state = set()
    for line in entries:
        coord = read_line(line)
        if coord in state:
            state.remove(coord)
        else:
            state.add(coord)
    
    neighbors = [(1,0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
    for day in range(100):
        next_state = set()
        to_check = set()
        for q, r in state:
            to_check.add((q,r))
            for dq, dr in neighbors:
                to_check.add((q + dq, r + dr))
        for q, r in to_check:
            count = sum(1 if (q + dq, r + dr) in state else 0 for dq, dr in neighbors)
            if (q, r) in state and count in (1, 2):
                next_state.add((q, r))
            elif (q, r) not in state and count == 2:
                next_state.add((q, r))
        state = copy.deepcopy(next_state)
    if day + 1 % 10 == 0:
        print(f"Day {day}, Number of black tiles : {len(state)}")
    return len(state)

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part1:", part1(entries))
    print("Answer for part2:", part2(entries))