from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self.arr = list()

    def get(self, obj):
        if Warehouse.valid(obj):
            self.arr.append(obj)
        else:
            print(f'Error: {self.__class__.__name__} takes only technics (\'{obj}\' was given)')

    def give(self, obj, where):
        return f'{self.arr.pop(self.arr.index(obj))} was given to \'{where}\''

    @staticmethod
    def valid(obj):
        return True if issubclass(obj.__class__, Technics) else False

class Technics(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__}-\'{self.name}\''


class Printer(Technics):
    def __init__(self, name):
        super().__init__(name)


class Scanner(Technics):
    def __init__(self, name, dpi):
        super().__init__(name)
        self.dpi = dpi


class Xerox(Technics):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color


p = Printer('p1')
print(p)
s = Scanner('s1', 300)
x = Xerox('x1', False)
w = Warehouse()
w.get('Smth')
w.get(s)
print(w.give(s, 'Sales'))
