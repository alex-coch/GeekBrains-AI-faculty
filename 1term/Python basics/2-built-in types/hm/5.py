# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
# тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
our_str = input('Enter your number: ')
if not our_str.isdigit():
    print('It isn\'t a number')
else:
    my_list.append(int(our_str))
    my_list.sort()
    my_list.reverse()
    print(my_list)