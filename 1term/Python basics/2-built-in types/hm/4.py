# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только
# первые 10 букв в слове.

our_list = input('Enter your string: ').split(' ')
count = 1
for item in our_list:
    if len(item) > 10:
        print(count, item[:10])
    else:
        print(count, item)
    count += 1