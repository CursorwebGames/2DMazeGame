import random
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
    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    def __init__(self, grid_size) -> None:
        self.grid_size = grid_size
        self.wall_size = SCREEN_SIZE // self.grid_size
        self.new_grid()

    def new_grid(self) -> None:
        self.grid = [[Cell() for _ in range(self.grid_size)]
                     for _ in range(self.grid_size)]

    def get_cell(self, row: int, col: int) -> Cell | None:
        if row < 0 or row >= self.grid_size or col < 0 or col >= self.grid_size:
            return None

        return self.grid[row][col]

    def valid(self, row: int, col: int, dir: tuple[int, int]) -> bool:
        cell = self.get_cell(row + dir[0], col + dir[1])

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

    def set_cell(self, row: int, col: int, dir: tuple[int, int]) -> bool:
        if not self.valid(row, col, dir):
            return False

        dr, dc = dir
        b1 = self.grid[row][col]
        b2 = self.grid[row + dr][col + dc]

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

    def gen_maze(self):
        visited: set[tuple[int, int]] = set()
        stack: list[tuple[int, int]] = []

        visited.add((0, 0))
        stack.append((0, 0))

        while len(stack):
            curr = stack.pop()
            row, col = curr

            if curr == (self.grid_size - 1, self.grid_size - 1):
                continue

            cdirs = self.dirs.copy()
            random.shuffle(cdirs)

            for dir in cdirs:
                next = (row + dir[0], col + dir[1])

                if next not in visited and self.set_cell(row, col, dir):
                    visited.add(next)
                    stack.append(curr)
                    stack.append(next)
                    break


class Mode(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def gen_icon() -> pygame.Surface: pass

    @abstractmethod
    def draw() -> None: pass
