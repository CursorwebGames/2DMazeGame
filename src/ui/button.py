import pygame

from defs import font, mx, my, screen

from . import colors


class ButtonStyle:
    Primary = 'Primary'
    Secondary = 'Secondary'


class Button:
    def __init__(self, text: str, x=0, y=0) -> None:
        self.text = font.render(text, True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()

        self.x, self.y = x, y

        self.collide_rect = pygame.rect.Rect(
            x, y, self.text_width + 20, self.text_height + 25)

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        self.collide_rect.move_ip(x, y)

    def draw(self):
        x, y = self.x, self.y
        if self.collide_rect.collidepoint(mx(), my()):
            pygame.draw.rect(screen, colors.Primary, (x, y + 5,
                             self.text_width + 20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (x + 10, y + 15))
        else:
            pygame.draw.rect(screen, colors.PrimaryAccent, (x, y + 5,
                             self.text_width + 20, self.text_height + 20), border_radius=5)
            pygame.draw.rect(screen, colors.Primary, (x, y, self.text_width +
                             20, self.text_height + 20), border_radius=5)
            screen.blit(self.text, (x + 10, y + 10))


class ButtonStackLayout:
    def __init__(self, x: int, y: int, *btns: Button, margin = 10):
        """
        Generate a vertical stack of buttons.
        The x is where the buttons should be aligned relative to their midpoints respectively.
        The y is the where the topmost line of the topmost button will be.
        """
        self.btns = btns

        y_pos = y

        for btn in btns:
            btn.move(x - btn.collide_rect.width // 2, y_pos)
            y_pos += btn.collide_rect.height + margin

    
    def draw(self):
        for btn in self.btns:
            btn.draw()