# def my_pow_fun(x, y):
#     try:
#         res = x ** y
#     except TypeError:
#         return "Ошибка"
#     return res


# def my_pow_fun(x, y):
#     try:
#         x, y = float(x), int(y)
#         if x <= 0 or y >= 0:
#             return 'Ошибка x должен быть больше 0, а y должен быть меньше 0'
#         else:
#             result = 1
#             for _ in range(abs(y)):
#                 result *= 1 / x
#             return f'результат возведения x в степень y: {round(result, 6)}'
#     except ValueError:
#         return "Программа работает только с числами."
#
# print(my_pow_fun(2, 2))


def my_pow_func(x, y):
    return 1 if y == 0 else my_pow_func(x, y + 1) * 1 / x

print(my_pow_func(2, -3))

