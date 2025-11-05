from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для HH"""

    @abstractmethod
    def __add__(self, other):
        pass
