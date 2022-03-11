'''5. Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.'''
abc_number = int(input('Введите номер буквы в алфавите: '))

# Генерация списка букв
abc_list = {i:chr(i) for i in range(ord('A'), ord('Z') + 1)}
print(abc_list)
if abc_number <= len(abc_list):
    # print(f'Буква под номером {abc_number}: {abc_list[abc_number - 1]}')
    print(f'Буква под номером {abc_number}: {chr(ord("A") - 1 + abc_number)}')
else:
    print(
      f'Введено число превышающее количество букв в алфавите ({len(abc_list)})'
    )
