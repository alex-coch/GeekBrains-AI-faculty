"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input("введите число(n)\n "
              "элементов ряда 1, -0.5, 0.25, -0.125, ..., n\n  "
              "a(i), a(i+1)= a(i)/(-2), a(i+2) = a(i+1)/(-2)... : "))
a = 1
enum = 0
sum_n = 0

while enum != n:
    sum_n += a
    a = a/(-2)
    enum += 1

print(f'Сумма {n}-элементов ряда = {sum_n}')
