# hm1 https://gb.ru/lessons/155978/homework
# task 1
x = int(input('Input a number: '))
s = input('Input a string: ')
print(x, s)

# task 2
x = int(input('Input  seconds: '))
print('%02d:%02d:%02d' % (x // 3600, x % 3600 // 60, x % 60))

# task 3
x = input('Input a number: ')
print(int(x) + int(x * 2) + int(x * 3))

# task 4
x = int(input('Input a number: '))
m = 0
while x != 0 and m != 9:
    if x % 10 > m:
        m = x % 10
    x //= 10
print(m)

# task 5
p = int(input('Input proceeds: '))
e = int(input('Input expenses: '))
if e > p:
    print('Losses')
else:
    print('Profit')
    x = int(input('Input amount of employees: '))
    print(f'Profit per an employee: {p / x}')

# task 6
a = int(input('Input a number a: '))
b = int(input('Input a number b: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f'{i} day')
