import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(B1, y=ks, X=zp, n=10):
    return np.sum((B1*X - y)**2)/n

alpha = 1e-6
B1 = 0.1
n = 10

for i in range(10):
    B1 -= alpha*(2/n)*np.sum((B1*zp - ks)*zp)
    print(f'{B1=}')

for i in range(100):
    B1 -= alpha*(2/n)*np.sum((B1*zp - ks)*zp)
    if (i%10 == 0):
        print(f'{i=} {B1=} mse={mse_(B1)}')

for i in range(3000):
    B1 -= alpha*(2/n)*np.sum((B1*zp - ks)*zp)
    if (i%500 == 0):
        print(f'{i=} {B1=} mse={mse_(B1)}')