'''Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.'''

from random import randint, uniform

type = input("Введите тип данных, где i-целое число/f-вещественное число/ c-символ: ")
start = input("Введите начальное значение: ")
end = input("Введите конечное значение: ")

if type == 'i':
    a = randint(int(start), int(end))
elif type == 'f':
    a = uniform(float(start), float(end))
elif type == 'c':
    a = chr(randint(ord(start), ord(end)))
else:
    a = f'Неизвестный тип данных {type}'

print(f'Случайное значение в диапазоне от {start} до {end} = {a}')
