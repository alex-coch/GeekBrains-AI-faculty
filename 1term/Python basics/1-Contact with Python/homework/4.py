# task 4
num1 = int(input('Input a number: '))
max_num = 0
while num1 != 0 and max_num != 9:
    if num1 % 10 > max_num:
        max_num = num1 % 10
    num1 //= 10
print(max_num)