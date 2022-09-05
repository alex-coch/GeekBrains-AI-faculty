arr = [8, 3, 15, 6, 4, -2, -8]


def mf(arr=None):
    mmin = min(arr)
    arr.remove(mmin)
    return mmin


print(mf(arr), mf(arr))
