# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию
# input().

our_list = []
while True:
    our_string = input('Enter new value (Type "Q" to exit): ')
    if our_string == 'Q':
        break
    else:
        our_list.append(our_string)
print('Start:', our_list)
our_len = len(our_list)
for item in range(0, our_len, 2):
    if our_len > 0 and item != (our_len - 1):
        our_list[item], our_list[item + 1] = our_list[item + 1], our_list[item]
print('Finish:', our_list)
