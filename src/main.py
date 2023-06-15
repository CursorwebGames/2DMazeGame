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

from utils import clock, screen, update_mouse_pos, event_handler, page, font
# from defs import clock, screen
# from events import update_mouse_pos, event_handler
# from page_state import page


class Main:
    """
    The Main game loop.
    This uses defs.py which is exposes internals to all other aspects of this game
    to run the game loop, handle events, etc.
    This should ONLY handle state, and shouldn't have any mutators.
    """
    def __init__(self) -> None:
        pass

    def loop(self) -> None:
        while True:
            clock.tick(70)
            self.draw()
            update_mouse_pos()
            self.handle_event()
            pygame.display.update()

    def draw(self) -> None:
        screen.fill("white")
        page.draw()
        
        t = font.render(str(int(clock.get_fps())), True, (0, 0, 0))
        screen.blit(t, (0, 0))

    def handle_event(self) -> None:
        for event in pygame.event.get():
            for evtype, fnarr in zip(event_handler.keys(), event_handler.values()):
                if event.type == evtype:
                    for fn in fnarr:
                        fn(event)

            if event.type == pygame.QUIT:
                sys.exit(0)


game = Main()
game.loop()
