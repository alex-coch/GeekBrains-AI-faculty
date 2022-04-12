# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

i = 1
for char in range(32, 128): # последний элемент не входит в список
    if i % 10 == 0: # выводим записи код-символ по 10 пар
        print(f'{char:7} - {chr(char)}')
    else:
        print(f'{char:7} -  {chr(char)}', end='')
    i += 1