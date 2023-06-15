from typing import Callable
from collections import defaultdict

import pygame

_mx = 0
_my = 0


def update_mouse_pos():
    global _mx, _my
    _mx, _my = pygame.mouse.get_pos()


def mx():
    return _mx


def my():
    return _my


event_handler: defaultdict[int, list[Callable[[pygame.event.Event], None]]] = defaultdict(lambda: [])

event_handler[pygame.KEYDOWN].append(lambda _: print(5))