from typing import Any, Callable

import pygame

from utils import event_handler, font, mx, my, screen

from . import colors


class ButtonStyle:
    Primary = 'Primary'
    Secondary = 'Secondary'
    Warning = 'Warning'

    @staticmethod
    def style_from(style: 'ButtonStyle'):
        match style:
            case ButtonStyle.Primary:
                return colors.Primary, colors.PrimaryAccent

            case ButtonStyle.Secondary:
                return colors.Secondary, colors.SecondaryAccent

            case ButtonStyle.Warning:
                return colors.Warning, colors.WarningAccent


class Button:
    def __init__(self,
                 text: str,
                 onclick: Callable[[], Any],
                 style: ButtonStyle = ButtonStyle.Primary,
                 font: pygame.font.Font = font,
                 x=0, y=0) -> None:
        self.text = font.render(text, True, (255, 255, 255))
        self.text_width, self.text_height = self.text.get_size()

        self.onclick = onclick
        event_handler[pygame.MOUSEBUTTONDOWN].append(self.handle)

        self.x, self.y = x, y
        self.main, self.accent = ButtonStyle.style_from(style)

        self.padding = 10
        self.width = self.text_width + 2 * self.padding
        self.height = self.text_height + 2 * self.padding

        self.collide_rect = pygame.rect.Rect(x, y, self.width, self.height + 5)

    def move(self, x: int, y: int):
        self.x, self.y = x, y
        self.collide_rect.move_ip(x, y)

    def resize(self, w: int, h: int = None):
        self.width = w + 2 * self.padding
        if h:
            self.height = h + 2 * self.padding

        self.collide_rect.width = self.width
        self.collide_rect.height = self.height + 5

    def draw(self):
        x, y = self.x, self.y
        if self.collide_rect.collidepoint(mx(), my()):
            pygame.draw.rect(screen, self.main,
                             (x, y + 5, self.width, self.height), border_radius=5)
            screen.blit(self.text, (x + (self.width - self.text_width) //
                        2, y + (self.height - self.text_height) // 2 + 5))
        else:
            pygame.draw.rect(screen, self.accent,
                             (x, y + 5, self.width, self.height), border_radius=5)
            pygame.draw.rect(screen, self.main,
                             (x, y, self.width, self.height), border_radius=5)
            screen.blit(self.text, (x + (self.width - self.text_width) //
                        2, y + (self.height - self.text_height) // 2))

    def handle(self, _: pygame.event.Event):
        left, _, _ = pygame.mouse.get_pressed()
        if left and self.collide_rect.collidepoint(mx(), my()):
            self.onclick()


class ButtonStackLayout:
    def __init__(self, x: int, y: int, *btns: Button):
        """
        Generate a vertical stack of buttons.
        The x is where the buttons should be aligned relative to their midpoints respectively.
        The y is the where the topmost line of the topmost button will be.
        """
        self.btns = btns

        y_pos = y
        margin = 10

        mw = -1

        for btn in btns:
            if btn.collide_rect.width > mw:
                mw = btn.collide_rect.width

        for btn in btns:
            btn.resize(mw)
            btn.move(x - btn.collide_rect.width // 2, y_pos)
            y_pos += btn.collide_rect.height + margin

    def draw(self):
        for btn in self.btns:
            btn.draw()
