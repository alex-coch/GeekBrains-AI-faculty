"""
��������� ��������� "������ ����������" ���������� O(n*log(n))
"""
def primes(n):
    a = [0] * n # �������� ������� � n ����������� ���������
    for i in range(n): # ���������� ������� ...
        a[i] = i # ���������� �� 0 �� n-1
     
    # ������ ��������� �������� �������, ������� �� ������� ������� ������
    # �������� �� �����.
    a[1] = 0
     
    m = 2 # ������ �� 0 ���������� � 3-�� �������� (������ ��� ��� ����)
    while m < n: # ������� ���� ��������� �� ��������� �����
        if a[m] != 0: # ���� �� �� ����� ����, ��
            j = m * 2 # ��������� � ��� ���� (������� ������� ������� �����)
            while j < n:
                a[j] = 0 # �������� �� 0
                j = j + m # ������� � ������� �� m ������
        m += 1
     
    # ����� ������� ����� �� ����� (����� ���� ���������� ��� ������)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
     
    del a
    return b

"""
��������� ��������� "������ ������" ���������� O(n)
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
  """���������� ��� ������� �� 2 �� N"""
  sieve = set(range(2, N))
  for i in range(2, int(math.sqrt(N))):
    if i in sieve:
      sieve -= set(range(2*i, N, i))
  return sieve
print primes(10)