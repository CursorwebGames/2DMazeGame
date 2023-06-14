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

visited: set[tuple[int, int]] = set()
stack: list[tuple[int, int]] = []

visited.add((1, 1))
stack.append((1, 1))

while len(stack) > 0:
    curr = stack.pop()
    print_maze(*curr)

    for dir in dirs:
        next = (curr[0] + dir[0], curr[1] + dir[1])

        if next not in visited and valid(curr[0], curr[1], dir):
            visited.add(next)
            stack.append(curr)
            stack.append(next)
            break
    
    input()
