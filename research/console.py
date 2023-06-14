from random import randint, choice
"""
1. Randomly select a node (or cell) N.
2. Push the node N onto a queue Q.
3. Mark the cell N as visited.
4. Randomly select an adjacent cell A of node N that has not been visited. If all the neighbors of N have been visited:
5. Continue to pop items off the queue Q until a node is encountered with at least one non-visited neighbor - assign this node to N and go to step 4.
6. If no nodes exist: stop.
7. Break the wall between N and A.
8. Assign the value A to N.
9. Go to step 2.
"""

SIZE = 17

grid = [None] * SIZE
# wall = True
for i in range(SIZE):
    grid[i] = [True] * SIZE

def random_point() -> tuple[int, int]:
    return randint(0, SIZE - 1), randint(0, SIZE - 1)

def get_cell(row: int, col: int) -> bool | None:
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return None
    return grid[row][col]

def valid(row: int, col: int, dir: tuple[int, int]) -> bool:
    return get_cell(row + 2 * dir[0], col + 2 * dir[1]) == True

def set_cell(row: int, col: int, dir: tuple[int, int]) -> bool:
    if not valid(row, col, dir): return False

    dr, dc = dir
    grid[row + dr][col + dc] = False
    grid[row + 2 * dr][col + 2 * dc] = False

    return True

dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

start_row, start_col = 1, 1 # random_point()
grid[start_row][start_col] = False

end_row, end_col = SIZE - 1, SIZE - 1

def gen_maze(row: int, col: int):
    if row == end_row and col == end_col: return
    cdirs = dirs.copy()
    dir = None
    # dir = choice(cdirs)
    # cdirs.remove(dir)

    while len(cdirs):
        dir = choice(cdirs)
        cdirs.remove(dir)
        # print('reach', dir, valid(row, col, dir))
        if set_cell(row, col, dir):
            gen_maze(row + 2 * dir[0], col + 2 * dir[1])



gen_maze(start_row, start_col)
# http://www.migapro.com/depth-first-search/

for row in grid:
    print(' '.join(map(lambda x : '#' if x else '-', row)))