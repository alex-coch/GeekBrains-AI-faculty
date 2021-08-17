# string = input("Введите слова через пробелы - ").split()
#
# for i, word in enumerate(string, 1):
#     print(i, word) if len(word) <= 10 else print(i, word[:10])



string = input("Введите слова через пробелы - ").split()
for i, word in enumerate(string, 1):
    print(f'{i}, {word[:10]}')
