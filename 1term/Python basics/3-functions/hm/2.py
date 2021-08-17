# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_print(name='', surname='', year='', city='', email='', phone=''):
    print(name, surname, year, city, email, phone, sep=', ')


arr = input('Enter name, surname, year, city, email, phone using comma as a determiner :').split(',')
if len(arr) == 6:
    my_print(*arr)
else:
    print('Some nonsense was given')
