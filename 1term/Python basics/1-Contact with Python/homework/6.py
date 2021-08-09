# task 6
num_a = int(input('Input a number a: '))
num_b = int(input('Input a number b: '))
count = 1
while num_a < num_b:
    num_a *= 1.1
    count += 1
print(f'{count} day(s)')
