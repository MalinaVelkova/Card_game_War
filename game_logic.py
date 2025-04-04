from abc import ABC, abstractmethod


class GameLogic(ABC):
    @abstractmethod
    def compare_cards(self):
        pass

    @abstractmethod
    def play_game(self):
        pass
