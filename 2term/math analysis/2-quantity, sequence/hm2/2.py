a = set('123')
b = set('234')

# union
un1 = a.union(b)
un2 = a | b
print(un1, un2)

# intersection
in1 = a.intersection(b)
in2 = a & b
print(in1, in2)

# difference
df1 = a.difference(b)
df2 = a - b
print(df1, df2)

# backward
df3 = b.difference(a)
df4 = b - a
print(df3, df4)

# symmetric difference
sd1 = a.symmetric_difference(b) # �������������� ��������
sd2 = a ^ b
print(sd1, sd2)

# empty sequence
c = set()
unc1 = a.union(c)
unc2 = b | c
print(unc1, unc2)

inc = a.intersection(c)
dfc = a.difference(c)
bdc = c.difference(a)
sdc = a.symmetric_difference(c)
# print(unc, inc, dfc, bdc, sdc)

# ��������� b � c
buc = b | c
bic = b & c
bdc = b - c
cdb = c - b
badc = b ^ c


# print(asdb)
# print(asdb1)