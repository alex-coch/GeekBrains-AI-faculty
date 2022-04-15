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

inc1 = a.intersection(c)
inc2 = b & c
print(inc1, inc2)

dfc1 = a.difference(c)
dfc2 = b - c
print(dfc1, dfc2)


bdc1 = c.difference(a)
bdc2 = c - b
print(bdc1, bdc2)


sdc1 = a.symmetric_difference(c)
sdc2 = b ^ c
print(sdc1, sdc2)
