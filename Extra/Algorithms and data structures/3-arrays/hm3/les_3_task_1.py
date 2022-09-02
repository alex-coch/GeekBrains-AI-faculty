for n in range(2, 10):
    print(f'{n}:', *(f for f in range(2, 100) if not (f % n)))
