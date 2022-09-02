arr = [8, 3, 15, 6, 4, 2]
index_min = min(range(len(arr)), key=arr.__getitem__)
index_max = max(range(len(arr)), key=arr.__getitem__)
arr[index_min], arr[index_max] = arr[index_max], arr[index_min]
print(arr)

