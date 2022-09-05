arr = [8, 3, 15, 6, 4, -2, -8]

mmax = max(arr)
mmin = min(arr)
print(sum([x for x in arr if x < mmax and x > mmin]))
