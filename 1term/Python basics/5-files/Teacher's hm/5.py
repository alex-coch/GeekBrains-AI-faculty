from random import randint
with open('5.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
