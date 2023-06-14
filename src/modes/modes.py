from pages import Menu


class GameMode:
    Classic = "Classic"
    Easy = "Easy"
    Fog = "Fog"
    PacMan = "PacMan"
    AIEasyRace = "AIEasyRace"
    AIHardRace = "AIHardRace"
    WASDRace = "WASDRace"

class Page:
    Menu = "Menu"
    Game = "Game"

class PageState:
    def __init__(self) -> None:
        self.page = Page.Menu
        self.game_mode = None
        self.paused = False

        self.menu = Menu()
    
    def draw(self):
        if self.page == Page.Menu:
            self.menu.draw()