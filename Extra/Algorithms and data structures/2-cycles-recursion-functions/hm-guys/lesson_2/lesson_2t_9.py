# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

list_num = [i for i in input('Введите несколько чисел в строку через пробел: ').split()]

print(list_num)
print(type(list_num))

def num_sum(num):
    summa = 0
    for j in num:
        summa += int(j)
    return summa

max_num = 0
max_sum = 0
for i in list_num:
    if num_sum(i) > max_sum:
        max_num = i
        max_sum = num_sum(i)


print(f'Ответ: число {max_num} имеет наибольшую сумму цифр: {max_sum}')