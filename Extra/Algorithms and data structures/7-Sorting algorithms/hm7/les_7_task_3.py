import random


def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    pivot = l[0]

    less = []
    more = []
    pivots = []
    for item in l:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > half:
        return median(less, half)
    elif len(less) + len(pivots) > half:
        return pivots[0]
    else:
        return median(more, half - len(more) - len(pivots))


n = 3
array = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(f'Исходный массив {array}')
print(f'Медиана {median(array, n)}')
