def sum_num():
    s = 0
    while True:
        in_list = input('Введите число или Q для выхода: ').split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:
                    s+= int(num)
                except ValueError:
                    print('Чтобы выйти из программы нажмите q - ')

        print(f'Сумма чисел = {s}')


num = 0
try:
    while num != 'q':
        for i in map(int, input('Для выхода наберите q Введите числе используя пробел - ').split()):
            num += i
        print(num)
except ValueError:
    print(num)