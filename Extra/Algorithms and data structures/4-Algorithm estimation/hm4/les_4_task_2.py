"""
Сложность алгоритма "решето Эратосфена" составляет O(n*log(n))
"""
def primes(n):
    a = [0] * n # создание массива с n количеством элементов
    for i in range(n): # заполнение массива ...
        a[i] = i # значениями от 0 до n-1
     
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
     
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n: # перебор всех элементов до заданного числа
        if a[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1
     
    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
     
    del a
    return b

"""
Сложность алогритма "Решето Аткина" составляет O(n)
"""
def atkins(limit):
    primes = [False] * limit
    sqrt_limit = int( math.sqrt( limit ) )

    x_limit = int( math.sqrt( ( limit + 1 ) / 2 ) )
    for x in xrange( 1, x_limit ):
        xx = x*x

        for y in xrange( 1, sqrt_limit ):
            yy = y*y

            n = 3*xx + yy
            if n <= limit and n%12 == 7:
                primes[n] = not primes[n]

            n += xx
            if n <= limit and n%12 in (1,5):
                primes[n] = not primes[n]

            if x > y:
                n -= xx + 2*yy
                if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]

    for n in xrange(5,limit):
        if primes[n]:
            for k in range(n*n, limit, n*n):
                primes[k] = False

    return [2,3] + filter(primes.__getitem__, xrange(5, limit))



def primes2(N):
  """Возвращает все простые от 2 до N"""
  sieve = set(range(2, N))
  for i in range(2, int(math.sqrt(N))):
    if i in sieve:
      sieve -= set(range(2*i, N, i))
  return sieve
print primes(10)