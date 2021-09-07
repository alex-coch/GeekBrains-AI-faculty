class Thingy:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num if self.num >= other.num else 'Operation isn\'t permitted'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num if other.num != 0 else 'Operation isn\'t permitted'

    def make_order(self, arg):
        res = '*****\n' * (int(self.num) // arg)
        if int(self.num) % arg != 0:
            res += '*' * (int(self.num) % arg) + '\n'
        print(res)


c1 = Thingy(1)
c2 = Thingy(2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c2 / c1)
c1. num = 12
c1.make_order(5)
