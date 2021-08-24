def fact(m):
    if m == 0:
        return 1
    else:
        return m * fact(m-1)


def gen(n):
    for el in range(1, n + 1):
        yield fact(el)


for i in gen(4):
    print(i)
