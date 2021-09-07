from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def get_count(self):
        pass


class Overcoat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def get_count(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def get_count(self):
        return self.height * 2 + 0.2


o = Overcoat(52)
s = Suit(180)
print(o.get_count + s.get_count)
