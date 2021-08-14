# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени
# года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

try:
    num = int(input('Enter number: '))
except:
    print('It isn\'t a number')
else:
    our_list = [(1, 2, 12), "winter", (3, 4, 5), "spring", (6, 7, 8), "summer", (9, 10, 11), "autumn"]
    for i in range(0, len(our_list), 2):
        if num in our_list[i]:
           print(our_list[i+1])
    our_dict = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'autumn': (9, 10, 11)}
    for season, months in our_dict.items():
        if num in months:
            print(season)