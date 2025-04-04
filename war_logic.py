from abc import ABC, abstractmethod


class WarLogic(ABC):
    @abstractmethod
    def war(self):
        pass
