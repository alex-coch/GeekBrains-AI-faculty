
while True:
    days = 1
    start_km = float(input('Начальный результат - '))
    last_km = float(input('Финальный результат - '))
    if start_km <= 0 or last_km < 0:
        print('Результаты должны быть больше нуля! Стартовое значение != 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
        print(f'Спрортмен добьется результат за {days} дней')


# Решение через рекурсию
# def km(res_min, res_max, days):
#     if res_min > res_max:
#         return days
#     else:
#         return km(res_min * 1.1, res_max, days + 1)

# print(km(int(input('Введите начальный результат'), int(input('Введите конечный результат')))))