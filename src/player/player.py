from abc import ABC, abstractmethod


@ABC
class Player:
    def __init__(self) -> None:
        super().__init__()
        self.x = 1
        self.y = 1

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def move(self):
        pass
