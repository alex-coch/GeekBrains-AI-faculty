#  В программе генерируется случайное целое число от 0 до 100.
#  Пользователь должен его отгадать не более чем за 10 попыток.
#  После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
#  чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random

namber = random.randint(1, 100)
i = 1

while i <= 10:
    user_namber = int(input('Введите число: '))
    print(user_namber)
    if namber == user_namber:
        print ('Победа!!!')
        break
    elif namber < user_namber:
        print('Ваше число больше, попробуйте еще раз...')
    else:
        print('Ваше число меньше, попробуйте еще раз...')
        i += 1
if i > 10:
    print(f'Не угадано! Загаданное число {namber}')



