from functools import reduce
from itertools import count, cycle


for el in count(3):
    if el > 10:
        break
    else:
        print(el, ' ', end='')
print()
c = 0
for el in cycle("xyz"):
    if c > 7:
        break
    print(el, ' ', end='')
    c += 1
