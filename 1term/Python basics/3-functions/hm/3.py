# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.

def my_func(a1, b1, c1):
    if (a1 >= c1) & (b1 >= c1):
        return a1 + b1
    elif (a1 >= b1) & (c1 >= b1):
        return a1 + c1
    else:
        return b1 + c1


print(my_func(3, 2, 1))
