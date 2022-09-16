'''
program outcomes:
insertion_sort 206
bsort2 209
selection_sort 217
sys.version_info(major=3, minor=9, micro=5, releaselevel='final', serial=0)
Windows 10

bsort2 - более эффективен
'''

import random
from random import randrange
import sys
import platform

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    print( insertion_sort.__name__, sum(list(map(sys.getsizeof,dir()))))
    return array

def bsort2(array):
    for i in range(len(array)):
        change = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                change = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not change:
            break
    print(bsort2.__name__, sum(list(map(sys.getsizeof,dir()))))
    return array

def selection_sort(input_list):
   for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
   input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
   print(selection_sort.__name__, sum(list(map(sys.getsizeof, dir()))))


arr = [randrange(0, 1000) for _ in range(1000)]
insertion_sort(arr)
bsort2(arr)
selection_sort(arr)
print(sys.version_info)
print(platform.system(), platform.release())

