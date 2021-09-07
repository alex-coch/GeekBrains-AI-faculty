class Matrix:
    def __init__(self, in_list):
        self.list = in_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list]))

    def __add__(self, other):
        res = Matrix([])
        for j in range(len(self.list)):
            temp = []
            for k in range(len(self.list[j])):
                x = self.list[j][k] + other.list[j][k]
                temp.append(x)
            res.list.append(temp)
        return res


m1 = Matrix([[1, 2], [3, 4]])
print(m1)
m2 = Matrix([[5, 6], [7, 8]])
m2 += m1
print(m2)
