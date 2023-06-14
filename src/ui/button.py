import pygame

from defs import screen, font, mx, my

from . import colors


class ButtonStyle:
    Primary = 'Primary'
    Secondary = 'Secondary'


class Button:
    def __init__(self, text: str) -> None:
        self.text = font.render(text, True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()
        self.collide_rect = None

    def draw(self, x: int, y: int):
        if not self.collide_rect:
            self.collide_rect = pygame.rect.Rect(
                x, y, self.text_width + 20, self.text_height + 25)
        if self.collide_rect.collidepoint(mx(), my()):
            pygame.draw.rect(screen, colors.Primary, (x, y + 5, self.text_width + 20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (x + 10, y + 15))
        else:
            pygame.draw.rect(screen, colors.PrimaryAccent, (x, y + 5, self.text_width + 20, self.text_height + 20), border_radius=5)
            pygame.draw.rect(screen, colors.Primary, (x, y, self.text_width + 20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (x + 10, y + 10))
