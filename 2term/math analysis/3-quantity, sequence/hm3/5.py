from sympy import factorial
import random


def f(n):
    return n / pow(factorial(n), 1 / n)


eps = 10 ** -7
i = 1
n = 1
x0 = f(n)
while True:
    i += 1
    n += random.randint(1, 100)
    x1 = f(n)
    if abs(x0 - x1) <= eps:
        break
    x0 = x1
print(f'n_iter: {i}')
print(f'f(n) = {x0}')