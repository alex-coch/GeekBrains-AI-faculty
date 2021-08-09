n = input("Введите положительное число - ")

while int(n) < 0:
    print('Я же сказал, ПОЛОЖИТЕЛЬНОЕ !!!')
    n = input("Введите положительное число - ")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
print()
