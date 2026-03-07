from typing import Union, List, Tuple, Optional
from pathlib import Path
from collections import defaultdict
from math import sqrt

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
TEST_FILE = SCRIPT_DIR / "test.txt"

def load_input(filepath: Union[str, Path]) -> List[Tuple[int, List[str]]]:
    """Returns the list of tiles as a list of tuples (tile_number, tile)"""
    tiles = []
    with open(filepath) as f:
        for tile in f.read().split('\n\n'):
            tile_number, image = tile.split(':\n')
            tile_number = int(tile_number[5:])
            image = image.split()
            tiles.append((tile_number, image))
    return tiles

def all_edges(piece: Tuple[int, List[str]]) -> Tuple[int, List[Tuple[str,...]]]:
    """From a piece, returns the edges in the form (top, right, bottom, left) (read from left to right and from top to bottom) 
    of all the permuations and the flips of the original piece"""
    n = len(piece[1])
    piece_id, chunck = piece
    t, b = chunck[0], chunck[-1]
    r, l = "", ""
    for i in range(n):
        r += chunck[i][-1]
        l += chunck[i][0]
    all_perm = [
        (t, r, b, l),
        (l[::-1], t, r[::-1], b),
        (b[::-1], l[::-1], t[::-1], r[::-1]),
        (r, b[::-1], l, t[::-1]),
        (t[::-1], l, b[::-1], r),
        (r[::-1], t[::-1], l[::-1], b[::-1]),
        (b, r[::-1], t, l[::-1]),
        (l, b, r, t)
    ]
    return (piece_id, all_perm)

def create_maps(entries: List[Tuple[int, List[str]]]):
    """Returns the top map and the left map so that we have a O(1) lookup map instead of looking through all the pieces each time"""
    top_map = defaultdict(list)
    left_map = defaultdict(list)
    for piece in entries:
        piece_id, all_perm = all_edges(piece)
        for perm in all_perm:
            t, r, b, l = perm
            top_map[t].append((piece_id, (t, r, b, l)))
            left_map[l].append((piece_id, (t, r, b, l)))
    return(top_map, left_map)

def create_all_pieces(entries: List[Tuple[int, List[str]]]):
    """Returns the list of all the pieces of this puzzle"""
    all_pieces = []
    for piece in entries:
        piece_id, all_perm = all_edges(piece)
        for perm in all_perm:
            all_pieces.append((piece_id, perm))
    return all_pieces

def part1(entries: List[Tuple[int, List[str]]]) -> Tuple[int, Optional[List]]:
    """Solves the puzzle and gives the product of the corners' id and the final grid in some orientation"""
    top_map, left_map = create_maps(entries)
    all_pieces = create_all_pieces(entries)
    grid_size = int(sqrt(len(entries)))
    grid = [[None] * grid_size for _ in range(grid_size)]
    used = set()
    def solve(pos: int) -> Tuple[bool, List[List[Optional[Tuple[int, Tuple[str,...]]]]]]:
        if pos == grid_size * grid_size:
            return True, grid # type: ignore
        needed_top, needed_left = None, None

        i, j = pos // grid_size, pos % grid_size
        if i > 0:
            needed_top = grid[i-1][j][1][2] # type: ignore
        if j > 0:
            needed_left = grid[i][j-1][1][1] # type: ignore
        
        candidates = set()
        if needed_top:
            candidates |= set(top_map[needed_top])
        else:
            candidates = all_pieces
        
        for piece_id, piece in candidates:
            if piece_id in used:
                continue
            
            t, r, b, l = piece

            if needed_left and l != needed_left:
                continue
            
            grid[i][j] = (piece_id, (t, r, b, l)) # type: ignore
            used.add(piece_id)

            if solve(pos + 1)[0]:
                return True, grid # type: ignore
            
            used.remove(piece_id)
        
        return False, None # type: ignore

    solved, final_grid = solve(0)
    if solved:
        return final_grid[0][0][0] * final_grid[0][-1][0] * final_grid[-1][0][0] * final_grid[-1][-1][0], final_grid # type: ignore
    else:
        return -1, None
    
def build_image(entries: List[Tuple[int, List[str]]], final_grid):
    tile_map = {tile_id: tile for tile_id, tile in entries}
    tile_inner_size = len(entries[0][1]) - 2

    def rotate(tile):
        return [''.join(row) for row in zip(*tile[::-1])]

    def flip(tile):
        return [row[::-1] for row in tile]

    def orientations(tile):
        t = tile
        for _ in range(4):
            yield t
            yield flip(t)
            t = rotate(t)

    def edges(tile):
        n = len(tile)
        top = tile[0]
        bottom = tile[-1]
        right = ''.join(tile[i][-1] for i in range(n))
        left = ''.join(tile[i][0] for i in range(n))
        return (top, right, bottom, left)

    def remove_borders(tile):
        return [row[1:-1] for row in tile[1:-1]]

    image = []

    for grid_row in final_grid:
        rows = [""] * tile_inner_size

        for tile_id, target_edges in grid_row:
            tile = tile_map[tile_id]

            for oriented in orientations(tile):
                if edges(oriented) == target_edges:
                    interior = remove_borders(oriented)
                    break

            for k in range(tile_inner_size):
                rows[k] += interior[k]

        image.extend(rows)

    return image

def part2(entries: List[Tuple[int, List[str]]]) -> int:
    """Counts the number of # that are not in the monsters"""
    sea_monster = [(1, 0), (2, 1), (2, 4), (1, 5), (1, 6), (2, 7), (2, 10), (1, 11), (1, 12), (2, 13), (2, 16), (1, 17), (0, 18), (1, 18), (1, 19)]
    monster_length = 20
    _, grid = part1(entries)
    image = build_image(entries, grid)
    count = sum([row.count("#") for row in image])
    
    def rotate_right(image: List[str]) -> List[str]:
        return ["".join(row) for row in zip(*image[::-1])]
    
    def all_rotations(image: List[str]) -> List[List[str]]:
        all_rot = []
        imageT = ["".join(row) for row in zip(*image)]
        for _ in range(4):
            all_rot.append(image)
            all_rot.append(imageT)
            image = rotate_right(image)
            imageT = rotate_right(imageT)
        return all_rot
    
    all_rot = all_rotations(image)
    for rot in all_rot:
        found_monster = False
        for i in range(len(image) - 2):
            for j in range(len(image[0]) - monster_length):
                complete_monster = True
                for (r, c) in sea_monster:
                    if rot[i + r][j + c] != "#":
                        complete_monster = False
                        break
                if complete_monster:
                    found_monster = True
                    count -= 15
        if found_monster:
            break
    return count

if __name__ == "__main__":
    entries = load_input(INPUT_FILE)
    print("Answer for part 1:", part1(entries)[0])
    print("Answer for part 2:", part2(entries))