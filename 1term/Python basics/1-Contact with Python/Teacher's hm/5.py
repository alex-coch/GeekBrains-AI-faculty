revenue = float(input("Введите занчение выручки - "))
costs = float(input("Введите занчение издержек - "))
result = revenue - costs
if result > 0:
    print(f"Поздарвляю! Ваша компания работает с прибылью {result} !")
    print(f"Рентабельность выручки - {result / revenue:.3f}")
    persons = int(input("Сколько счастливых целых сотрудников работает в вашей комапании? - "))
    print(f"Прибыль на одного сотрудника - {result / persons:.3f}")
elif result < 0:
    print(f"Вы работаете с убытком - {-result}")
else:
    print(f"Ноль - это тоже хороший результат! Зато стабильно!")
