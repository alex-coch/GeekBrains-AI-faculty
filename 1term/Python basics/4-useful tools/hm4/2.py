m = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print( [m[i] for i in range(1, len(m)) if m[i] > m[i-1] ] )