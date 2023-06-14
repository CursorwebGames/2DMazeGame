import pygame
import random
import sys

# setup
pygame.init()
pygame.font.init()


# config
SCREEN_SIZE = 500
SIZE = 5
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


dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
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
    if grid[p_row + dr][p_col + dc] == False:
        p_row += dr
        p_col += dc


gen_maze(start_row, start_col)

# defs
font = pygame.font.SysFont('Arial', 16)
clock = pygame.time.Clock()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gaming!")


# pygame.key.set_repeat(100, 5)

while True:
    clock.tick(70)

    screen.fill('white')

    for i in range(SIZE):
        for j in range(SIZE):
            cell = grid[i][j]
            if cell:
                pygame.draw.rect(
                    screen, (0, 0, 0), (i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    pygame.draw.rect(screen, (255, 255, 0), (end_row * WALL_SIZE, end_col * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    # player
    pygame.draw.rect(screen, (255, 0, 0), (p_row * WALL_SIZE,
                     p_col * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    fog = pygame.Surface((width, height))
    fog.fill((123, 123, 123))
    pygame.draw.circle(fog, (0, 0, 0), (p_row * WALL_SIZE + WALL_SIZE // 2, p_col * WALL_SIZE + WALL_SIZE // 2), WALL_SIZE * VISIBLE)
    fog.set_colorkey((0, 0, 0))
    screen.blit(fog, (0, 0))
    # pygame.draw.circle(screen, (123, 123, 123), (p_row * WALL_SIZE + WALL_SIZE // 2, p_col * WALL_SIZE + WALL_SIZE // 2), WALL_SIZE * VISIBLE, 500)

    # key_pressed = False

    # keys = defaultdict(lambda: False)

    for event in pygame.event.get():
        # if event.type == pygame.KEYDOWN:
            # key_pressed = True
            # keys[event.key] = True
                    
            # if event.key == pygame.K_LEFT:
            #     move(-1, 0)
            # if event.key == pygame.K_RIGHT:
            #     move(1, 0)
            # if event.key == pygame.K_UP:
            #     move(0, -1)
            # if event.key == pygame.K_DOWN:
            #     move(0, 1)

        if event.type == pygame.QUIT:
            sys.exit(0)

    # if not key_pressed:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        move(-1, 0)
    if keys[pygame.K_RIGHT]:
        move(1, 0)
    if keys[pygame.K_UP]:
        move(0, -1)
    if keys[pygame.K_DOWN]:
        move(0, 1)

    if (p_row, p_col) == (end_row, end_col):
        SIZE += 2
        WALL_SIZE = SCREEN_SIZE // SIZE

        p_row, p_col = 1, 1
        grid[start_row][start_col] = False

        end_row, end_col = SIZE - 2, SIZE - 2

        grid = new_grid()
        gen_maze(start_row, start_col)

    pygame.display.update()
