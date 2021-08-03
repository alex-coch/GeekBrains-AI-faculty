true_password = 'qwerty'
password = input('Введтие пароль - ')

if true_password == password:
    print('Пароль верный')
    print('Доступ разрешен!')

else:
    print('Пароль неверный!')
    print('Доступ запрещен!')

print('конец программы')
