class GameMode:
    Classic = "Classic"
    Easy = "Easy"
    Fog = "Fog"
    PacMan = "PacMan"
    AIEasyRace = "AIEasyRace"
    AIHardRace = "AIHardRace"
    WASDRace = "WASDRace"

class PageName:
    Menu = "Menu"
    Select = "Select"
    Game = "Game"

_curr_page = PageName.Menu

def change_page(page):
    global _curr_page
    _curr_page = page

def curr_page():
    return _curr_page