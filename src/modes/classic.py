import pygame

from .mode import Mode


class Classic(Mode):
    def __init__(self) -> None:
        super().__init__()

    def gen_icon() -> pygame.Surface:
        out = pygame.Surface()

        out.blit("lmao")
