# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(a1, b1):
    return a1 / b1


try:
    a = float(input('Enter a: '))
    b = float(input('Enter b (not 0): '))
    assert b != 0
except (ValueError, AssertionError):
    print('Incorrect variables')
else:
    print(div(a, b))
