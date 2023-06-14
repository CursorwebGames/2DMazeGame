import pygame
import random
import time
import sys

# setup
pygame.init()
pygame.font.init()


# config
SCREEN_SIZE = 500
SIZE = 15
WALL_SIZE = SCREEN_SIZE // SIZE
VISIBLE = 3
width, height = SCREEN_SIZE, SCREEN_SIZE

grid = []


def new_grid():
    return [[True] * SIZE for _ in [None] * SIZE]


grid = new_grid()


def get_cell(row: int, col: int) -> bool | None:
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return None
    return grid[row][col]


def valid(row: int, col: int, dir: tuple[int, int]) -> bool:
    return get_cell(row + 2 * dir[0], col + 2 * dir[1]) == True


def set_cell(row: int, col: int, dir: tuple[int, int]) -> bool:
    if not valid(row, col, dir):
        return False

    dr, dc = dir
    grid[row + dr][col + dc] = False
    grid[row + 2 * dr][col + 2 * dc] = False

    return True


dirs: list[tuple[int, int]] = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

start_row, start_col = 1, 1
p_row, p_col = 1, 1
grid[start_row][start_col] = False

end_row, end_col = SIZE - 2, SIZE - 2


def gen_maze(row: int, col: int):
    if row == end_row and col == end_col:
        return
    cdirs = dirs.copy()
    dir = None

    while len(cdirs):
        dir = random.choice(cdirs)
        cdirs.remove(dir)

        if set_cell(row, col, dir):
            gen_maze(row + 2 * dir[0], col + 2 * dir[1])


def move(dr: int, dc: int):
    global p_row, p_col
    p_row += dr
    p_col += dc
    time.sleep(0.5)


def valid_move(row: int, col: int, dir: tuple[int, int]):
    dr, dc = dir
    dr += row
    dc += col
    return (dr, dc) not in visited and get_cell(dr, dc) == False

"""
# def solve_maze(visited: set[tuple[int, int]] = set(), prev_dir: tuple[int, int] = None):
#     if p_row == end_row and p_col == end_col:
#         return
    
#     visited.add((p_row, p_col))

#     made_move = False

#     for dir in dirs:
#         if valid_move(*dir):
#             made_move = True
#             move(*dir)
#             # solve_maze(visited, dir)
    
#     if not made_move and prev_dir != None:
#         move(-prev_dir[0], -prev_dir[1])
"""

visited: set[tuple[int, int]] = set()
stack: list[tuple[int, int]] = []

visited.add((p_row, p_col))
stack.append((p_row, p_col))

def next_move():
    global p_row, p_col
    curr = stack.pop()
    p_row, p_col = curr

    for dir in dirs:
        if valid_move(*curr, dir):
            next = (curr[0] + dir[0], curr[1] + dir[1])
            visited.add(next)
            stack.append(curr)
            stack.append(next)
            break

gen_maze(start_row, start_col)

# defs
font = pygame.font.SysFont('Arial', 16)
clock = pygame.time.Clock()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gaming!")

while True:
    clock.tick(70)

    screen.fill('white')

    for i in range(SIZE):
        for j in range(SIZE):
            cell = grid[i][j]
            if cell:
                pygame.draw.rect(
                    screen, (0, 0, 0), (i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    pygame.draw.rect(screen, (255, 255, 0), (end_row * WALL_SIZE,
                     end_col * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    # player
    pygame.draw.rect(screen, (255, 0, 0), (p_row * WALL_SIZE,
                     p_col * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    pygame.time.delay(50)
    if (p_row, p_col) == (end_row, end_col):
        SIZE += 2
        WALL_SIZE = SCREEN_SIZE // SIZE

        p_row, p_col = 1, 1
        visited = set()
        stack = []
        visited.add((p_row, p_col))
        stack.append((p_row, p_col))

        grid[start_row][start_col] = False

        end_row, end_col = SIZE - 2, SIZE - 2

        grid = new_grid()
        gen_maze(start_row, start_col)
    else:
        next_move()
    pygame.display.update()
