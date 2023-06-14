import pygame

from defs import screen, font, mx, my

from . import colors


class ButtonStyle:
    Primary = 'Primary'
    Secondary = 'Secondary'

class Button:
    def __init__(self, x: int, y: int, text: str) -> None:
        self.x = x
        self.y = y
        self.text = font.render(text, True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()

        self.collide_rect = pygame.rect.Rect(self.x, self.y, self.text_width + 20, self.text_height + 25)
    
    def draw(self):
        if self.collide_rect.collidepoint(mx(), my()):
            pygame.draw.rect(screen, colors.Primary, (self.x, self.y + 5, self.text_width + 20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (self.x + 10, self.y + 15))
        else:
            pygame.draw.rect(screen, colors.PrimaryAccent, (self.x, self.y + 5, self.text_width + 20, self.text_height + 20), border_radius=5)
            pygame.draw.rect(screen, colors.Primary, (self.x, self.y, self.text_width + 20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (self.x + 10, self.y + 10))