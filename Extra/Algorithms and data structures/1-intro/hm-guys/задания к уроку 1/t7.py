'''Определить, является ли год, который ввел пользователь,
високосным или не високосным.
'''

year = int(input('Введите год в формате гггг: '))
if year % 4 == 0:
    print(f'Год {year} - високосный')
else:
    print(f'Год {year} - не високосный')