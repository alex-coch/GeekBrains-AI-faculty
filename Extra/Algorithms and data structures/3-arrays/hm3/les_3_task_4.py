import collections


arr = [8, 3, 15, 6, 4, 2, 8]
print(max(collections.Counter(arr), key=arr.get))