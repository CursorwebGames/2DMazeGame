maze = list(map(list, """
###########
# #   #  .#
# # # # ###
#   #     #
# ####### #
#    #    #
###########
""".strip().split("\n")))

WIDTH = len(maze[0])
HEIGHT = len(maze)

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def valid(row, col, dir):
    dr, dc = dir
    dr += row
    dc += col
    return dr >= 0 and dr < HEIGHT and dc >= 0 and dc < WIDTH and maze[dr][dc] != '#'

def print_maze(row, col):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i == row and j == col:
                print('%', end='')
            else:
                print(maze[i][j], end='')
        print()

def get_end():
    for i in range(1, HEIGHT - 1):
        for j in range(1, WIDTH - 1):
            if maze[i][j] == '.':
                return i, j

visited: set[tuple[int, int]] = set()
queue: list[tuple[int, int]] = []
parent: dict[tuple[int, int], tuple[int, int]] = {}

visited.add((1, 1))
queue.append((1, 1))

while len(queue) > 0:
    curr = queue.pop(0)
    if maze[curr[0]][curr[1]] == '.':
        break

    for dir in dirs:
        next = (curr[0] + dir[0], curr[1] + dir[1])

        if next not in visited and valid(curr[0], curr[1], dir):
            visited.add(next)
            queue.append(next)
            parent[next] = curr
    
    # input()

path = []

curr = get_end()
while curr in parent:
    path.insert(0, curr)
    curr = parent[curr]

for p in path:
    print_maze(*p)
    input()