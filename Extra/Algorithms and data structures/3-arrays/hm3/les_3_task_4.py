import collections


arr = [8, 3, 15, 6, 4, 2, 8]
print(collections.Counter(arr).most_common(1)[0][0], max(set(arr), key = arr.count))