"""
Сложность алгоритма "решето Эратосфена" составляет O(n*log(n))
"""

import math

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


def SieveOfAtkin(limit):
    # 2 and 3 are known
    # to be prime
    if limit > 2:
        print(2, end=" ")
    if limit > 3:
        print(3, end=" ")

    # Initialise the sieve
    # array with False values
    sieve = [False] * (limit + 1)
    for i in range(0, limit + 1):
        sieve[i] = False

    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                    n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r <= limit:
        if sieve[r]:
            for i in range(r * r, limit + 1, r * r):
                sieve[i] = False

        r += 1


    for a in range(5, limit + 1):
        if sieve[a]:
            print(a, end=" ")




print(primes(10))
print(SieveOfAtkin(10))
