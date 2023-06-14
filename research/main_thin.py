import pygame
import random
import sys

# setup
pygame.init()
pygame.font.init()


# config
SCREEN_SIZE = 500
SIZE = 55
WALL_SIZE = SCREEN_SIZE // SIZE
STROKE = 1
width, height = SCREEN_SIZE, SCREEN_SIZE

grid = []


class Box:
    def __init__(self) -> None:
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
    
    def draw(self, row: int, col: int) -> None:
        if self.left:
            pygame.draw.line(screen, (0, 0, 0), (col, row), (col, row + WALL_SIZE), STROKE)
        if self.right:
            pygame.draw.line(screen, (0, 0, 0), (col + WALL_SIZE, row), (col + WALL_SIZE, row + WALL_SIZE), STROKE)
        if self.top:
            pygame.draw.line(screen, (0, 0, 0), (col, row), (col + WALL_SIZE, row), STROKE)
        if self.bottom:
            pygame.draw.line(screen, (0, 0, 0), (col, row + WALL_SIZE), (col + WALL_SIZE, row + WALL_SIZE), STROKE)
            

def new_grid():
    out: list[list[Box]] = []
    for _ in range(SIZE):
        arr = []
        for _ in range(SIZE):
            arr.append(Box())
        out.append(arr)
    return out


grid = new_grid()

def get_cell(row: int, col: int) -> Box | None:
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return None
    return grid[row][col]


def valid(row: int, col: int, dir: tuple[int, int]) -> bool:
    cell = get_cell(row + dir[0], col + dir[1])

    if not cell:
        return False

    match dir:
        case (1, 0):
            return cell.bottom == True
        case (-1, 0):
            return cell.top == True
        case (0, 1):
            return cell.left == True
        case (0, -1):
            return cell.right == True


def set_cell(row: int, col: int, dir: tuple[int, int]) -> bool:
    if not valid(row, col, dir):
        return False

    dr, dc = dir
    b1 = grid[row][col]
    b2 = grid[row + dr][col + dc]

    match dir:
        case (1, 0):
            b2.top = b1.bottom = False
        case (-1, 0):
            b2.bottom = b1.top = False
        case (0, 1):
            b2.left = b1.right = False
        case (0, -1):
            b2.right = b1.left = False

    return True


dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

start_row, start_col = 0, 0
p_row, p_col = 0, 0


end_row, end_col = SIZE - 1, SIZE - 1


def gen_maze():
    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = []

    visited.add((p_row, p_col))
    stack.append((start_row, start_col))

    while len(stack):
        curr = stack.pop()
        row, col = curr

        if curr == (end_row, end_col):
            continue
        
        cdirs = dirs.copy()
        random.shuffle(cdirs)

        for dir in cdirs:
            next = (row + dir[0], col + dir[1])

            if next not in visited and set_cell(row, col, dir):
                visited.add(next)
                stack.append(curr)
                stack.append(next)
                break


def move(dr: int, dc: int):
    global p_row, p_col

    box = get_cell(p_row, p_col)

    if not box: return

    match (dr, dc):
        case (1, 0):
            wall = box.bottom
        case (-1, 0):
            wall = box.top
        case (0, 1):
            wall = box.right
        case (0, -1):
            wall = box.left
    if not wall:
        p_row += dr
        p_col += dc


gen_maze()

# defs
font = pygame.font.SysFont('Arial', 16)
clock = pygame.time.Clock()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gaming!")


pygame.key.set_repeat(100, 15)

# set_cell(0, 0, (1, 0))
# set_cell(0, 0, (0, 1))

while True:
    clock.tick(70)

    screen.fill('white')

    for i in range(SIZE):
        for j in range(SIZE):
            cell = grid[i][j]
            cell.draw(i * WALL_SIZE, j * WALL_SIZE)

    # goal
    pygame.draw.rect(screen, (255, 255, 0), (end_col * WALL_SIZE + STROKE // 2,
                     end_row * WALL_SIZE + STROKE // 2, WALL_SIZE - STROKE, WALL_SIZE - STROKE))


    # player
    pygame.draw.rect(screen, (255, 0, 0), (p_col * WALL_SIZE + STROKE // 2,
                     p_row * WALL_SIZE + STROKE // 2, WALL_SIZE - STROKE, WALL_SIZE - STROKE))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move(0, -1)
            if event.key == pygame.K_RIGHT:
                move(0, 1)
            if event.key == pygame.K_UP:
                move(-1, 0)
            if event.key == pygame.K_DOWN:
                move(1, 0)

        if event.type == pygame.QUIT:
            sys.exit(0)

    if (p_row, p_col) == (end_row, end_col):
        SIZE += 2
        WALL_SIZE = SCREEN_SIZE // SIZE

        p_row, p_col = 0, 0

        end_row, end_col = SIZE - 1, SIZE - 1

        grid = new_grid()
        gen_maze()

    pygame.display.update()
