import random

import pygame

from utils import WIDTH, screen
from ui import Button, ButtonStackLayout

from .page import Page


class Menu(Page):
    def __init__(self) -> None:
        super().__init__()
        self.title_font = pygame.font.SysFont("candara", 100, True)
        self.menu_layout = ButtonStackLayout(
            WIDTH / 2, 150,
            Button('Play'),
            Button('Settings'),
            Button('Quit')
        )

        self.title = self.title_font.render("Pyrinth", True, (0, 0, 0))
        self.title_width, self.title_height = self.title.get_size()

        size = 2

        for i in range(0, self.title_width, size):
            for j in range(0, self.title_height, size):
                if random.randint(1, 2) == 1:
                    pygame.draw.rect(
                        self.title, (255, 255, 255), (i, j, size, size))

        self.title.set_colorkey((255, 255, 255))

    def draw(self) -> None:
        screen.blit(self.title, ((WIDTH - self.title_width) / 2, 50))
        self.menu_layout.draw()
