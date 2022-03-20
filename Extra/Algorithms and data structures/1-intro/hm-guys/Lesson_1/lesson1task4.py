start = input('Введите первую букву: ')
stop = input('Введите вторую букву: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(f'Первая буква стоит на позиции: {alphabet.find(start) + 1}')
print(f'Вторая буква стоит на позиции: {alphabet.find(stop) + 1}')
print(f'Между ними {abs(alphabet.find(stop) - alphabet.find(start) - 1)} буквы')