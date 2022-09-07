"""
Пузырьковая - O(n^2)
Вставками - O(n^2)
Быстрая - O(n*log(n))

c. оптимальный  - быстрая сортировка
e. вывод  - https://habr.com/ru/post/188010/
Function 'insertion_sort' executed in 14.7574s
Function 'bsort2' executed in 24.4607s
Function quicksort executed in 0.1530s
"""

import random
from random import randrange
from time import time


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_func
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


@timer_func
def bsort2(array):
    for i in range(len(array)):
        change = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                change = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not change:
            break
    return array


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


def quicksort2(nums, fst, lst):
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort2(nums, fst, j)
    quicksort2(nums, i, lst)


arr = [randrange(0, 10000) for _ in range(10000)]
arr1 = insertion_sort(arr[:])
arr2 = bsort2(arr[:])
t1 = time()
# arr3 = arr[:]
arr3 = quicksort(arr[:])
t2 = time()
print(f'Function quicksort executed in {(t2 - t1):.4f}s')
print(arr3 == arr2, arr1 == arr3)
