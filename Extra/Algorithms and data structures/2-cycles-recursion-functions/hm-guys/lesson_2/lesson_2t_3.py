# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num_1 = int(input('Введите целое число: '))
num_2 = 0
while num_1 > 0:
    i = num_1 % 10 #возьмём последнюю цифру - остаток от деления на 10
    num_1 = num_1 // 10 #получим остаток от деления нацело введённого числа на 10
    num_2 = num_2 * 10 #умножим искомое число на 10
    num_2 = num_2 + i #полученный остаток прибавим к искомому числу
print(num_2)