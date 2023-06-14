from defs import font, screen
from ui import Button

from .page import Page


class Menu(Page):
    def __init__(self) -> None:
        super().__init__()        
        self.button = Button(50, 50, 'Hello, world!')
    
    def draw(self) -> None:
        self.button.draw()