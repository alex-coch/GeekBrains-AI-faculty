#4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125, 0.0625...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов n = '))
total = 1
num = 1
while n > 1:
    num = num * -0.5
    total = total + num
    n -= 1
print(f'Сумма элементов ряда чисел равна: {total}')
