# my_list = list(input("Введите числа без пробелов - "))
#
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
# print(my_list)

#--------------------------------------------------------------------------------------------

# a = input('Введите элементы для массива разделяя их пробелами: ').split()
# i = 0
# print(f'Оригинальный список {a}')
# while i + 1 < len(a):
#     if i % 2 == 0:
#         a.insert(i, a.pop(i + 1))
#     i += 1
# print(f'Измененный список {a}')


#---------------------------------------------------------------------------------------------

user_list = input('Введите числа с пробелами - ').split()

for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)

