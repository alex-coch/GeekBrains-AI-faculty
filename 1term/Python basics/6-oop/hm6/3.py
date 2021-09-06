class Worker:
    def __init__(self, name, surname, position, income):
        self.fname = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        # print(name, args, kwargs)
        # super().__init__(name, surname, position, income)
        super(Position, self).__init__(name, surname, position, income)

    def get_full_name(self):
        return self.fname + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


chief = Position('Alex', 'Coch', 'Miner', {'wage': 100, 'bunus': 13})
print(chief.get_full_name(), chief.get_total_income())
