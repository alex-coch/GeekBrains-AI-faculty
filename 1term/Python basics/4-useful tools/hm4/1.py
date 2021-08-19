from sys import argv
try:
    arr = list(map(int, argv[1:]))
    assert len(arr) == 3
except (ValueError, AssertionError):
    print('Some nonsense was given')
else:
    print(arr[0] * arr[1] + arr[2])
