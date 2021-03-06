# 7. Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
n = int(input('Введите натуральное число n = '))

total_1 = 0
total_2 = n * (n + 1) / 2

for i in range(n):
    total_1 = total_1 + (i + 1)

print(f'Сумма элементов множества поэлементно равна: {total_1}')
print(f'Сумма элементов множества согласно равенства равна: {int(total_2)}')
if total_1 - total_2 == 0:
    print('Равенство выполняется!')
else:
    print('Равенство не выполняется!')