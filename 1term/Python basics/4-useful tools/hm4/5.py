from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


print(reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))
