from itertools import compress
from math import ceil
from time import time


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


"""
Сложность алгоритма "решето Эратосфена" составляет O(n*log(n))
"""


@timer_func
def primes(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


"""
Сложность алогритма "Решето Аткина" составляет O(n)
"""


@timer_func
def sieve(limit):
    if limit < 2:
        return []

    limit += 1  # Preincrement `limit` so sieve is inclusive, unlike `range`.
    primes = [True] * limit
    for base in range(2, int(limit ** 0.5 + 1)):
        if primes[base]:
            primes[base * 2:limit:base] = [False] * (ceil(limit / base) - 2)

    primes[0] = primes[1] = False
    return compress(range(limit), primes)


primes(1000000)
sieve(1000000)
