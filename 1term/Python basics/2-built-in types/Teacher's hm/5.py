my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = int(input('Введите новый элемент рейтига в виде натурального числа - '))
i = 0

for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, float(new_number))
print(my_list)