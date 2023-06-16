from abc import ABC, abstractmethod

import pygame

from utils import SCREEN_SIZE, screen


class Cell:
    wall_size = 1
    stroke = 1

    def __init__(self) -> None:
        self.left = True
        self.right = True
        self.top = True
        self.bottom = True
    
    @staticmethod
    def set_wall_size(size: int):
        Cell.wall_size = size

    def draw(self, row: int, col: int) -> None:
        if self.left:
            pygame.draw.line(screen, (0, 0, 0), (col, row),
                             (col, row + self.wall_size), self.stroke)
        if self.right:
            pygame.draw.line(screen, (0, 0, 0), (col + self.wall_size, row),
                             (col + self.wall_size, row + self.wall_size), self.stroke)
        if self.top:
            pygame.draw.line(screen, (0, 0, 0), (col, row),
                             (col + self.wall_size, row), self.stroke)
        if self.bottom:
            pygame.draw.line(screen, (0, 0, 0), (col, row + self.wall_size),
                             (col + self.wall_size, row + self.wall_size), self.stroke)


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


class Mode(ABC):
    @abstractmethod
    def icon() -> pygame.Surface: pass

    @abstractmethod
    def draw() -> None: pass
