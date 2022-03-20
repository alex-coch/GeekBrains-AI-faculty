# 8. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).
print('Введите три числа!')
my_array = []
my_array.append(float(input("Введите первое число = ")))
my_array.append(float(input("Введите второе число = ")))
my_array.append(float(input("Введите третье число = ")))

print(f'Средним числом будет {sorted(my_array)[1]}')