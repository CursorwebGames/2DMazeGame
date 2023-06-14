"""
Game modes:
    * Classic -- Play until you don't want to?
    * Speed Round -- Play until you can't solve the level in under 1 minute
    * Fog of War
    * Pac Man (multiple coins)
    * Race against AI (smart vs dumb)
    * Race against other human WASD vs arrow
"""
import sys

import pygame

from defs import clock, screen, update_mouse_pos
from modes.modes import GameMode, Page, PageState


class Main:
    screen_size = width = height = 600

    def __init__(self) -> None:
        self.page = PageState()

    def loop(self) -> None:
        while True:
            clock.tick(70)
            self.draw()
            update_mouse_pos()
            self.handle_event()
            pygame.display.update()

    def draw(self) -> None:
        screen.fill("white")
        self.page.draw()

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


game = Main()
game.loop()
