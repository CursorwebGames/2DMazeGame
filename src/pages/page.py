from abc import ABC, abstractmethod


class Page(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def draw(self) -> None:
        pass