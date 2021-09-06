class Road:
    _length = 0
    _width = 0

    def __init__(self, len1, wid1):
        Road._length = len1
        Road._width = wid1

    @staticmethod
    def get_mas(mas1, thn1):
        return Road._length * Road._width * mas1 * thn1


road1 = Road(20, 5000)
print(round(road1.get_mas(25, 5) / 1000, 3), 'т')
