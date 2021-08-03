true_password = 'qwerty'

max_mistakes = 3
current_attempt = 1


while True:
    user_password = input('Введите пароль - ')

    if user_password == true_password:
        print('Доступ разрешен!')
        break

    if current_attempt == max_mistakes:
        print('Все попытки исчерпаны. Досутп запрещен!')
        break

    remaining_attempts = max_mistakes - current_attempt
    print(f'Пароль введен неверно! Осталось попыток {remaining_attempts}')
    current_attempt += 1


