from utils import screen, font
from .page import Page

class Select(Page):
    def __init__(self) -> None:
        super().__init__()
        self.text = font.render("Select Game!", True, (0, 0, 0))
    
    def draw(self) -> None:
        screen.blit(self.text, (50, 50))