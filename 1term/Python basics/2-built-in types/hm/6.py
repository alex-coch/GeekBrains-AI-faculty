# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
# пользователя.

our_list = []
count = 0
while True:
    in_list = input('Enter "название", "компьютер", "цена", "ед" dividing meanings with comma (Q - exit): ').split(',')
    [item.strip() for item in in_list]
    if in_list[0] == 'Q':
        break
    our_list.append((count+1, {'название': in_list[0], 'цена': round(float(in_list[1]), 2),
                               'количество': int(in_list[2]), 'ед': in_list[3]}))
    count += 1
outcome = {'название': [], 'цена': [], 'количество': [], 'ед': []}
for item in our_list:
    for key, value in item[1].items():
        outcome[key].append(value)
print(outcome)
