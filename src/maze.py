from defs import SCREEN_SIZE


class Maze:
    def __init__(self) -> None:
        self.grid_size = 5  # must be odd!
        self.wall_size = SCREEN_SIZE // self.grid_size
        self.new_grid()

    def new_grid(self) -> None:
        self.grid = [[True] * self.grid_size for _ in [None] * self.grid_size]

    def get_cell(self, row: int, col: int) -> None:
        if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
            return None

        return self.grid[row][col]
