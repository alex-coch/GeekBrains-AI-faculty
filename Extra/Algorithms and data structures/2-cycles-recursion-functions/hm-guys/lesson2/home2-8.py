# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

user_renge = input('Введите последовательность чисел: ')
user_num = input('Введите цифру для поиска: ')
count = 0
for i in user_renge:
    if i == user_num:
        count += 1

print(f'Цифра {user_num} встречается в последоватедльности {user_renge} {count} раз(a)')
