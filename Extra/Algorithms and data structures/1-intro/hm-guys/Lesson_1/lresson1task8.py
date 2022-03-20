a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c:
    print(a)

if c < a < b:
    print(a)

if a < b < c:
    print(b)

if c < b < a:
    print(b)

if a < c < b:
    print(b)

if b < c < a:
    print(a)