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

curr_page = PageName.Menu

def change_page(page):
    global curr_page
    curr_page = page