import numpy as np
from scipy import stats

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182])
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
n1 = len(y1)
n2 = len(y2)
n3 = len(y3)

Fn = stats.f_oneway(y1, y2, y3)[0]
Fcrit=3.337  # regarding the Fisher's table
print('n=',n1+n2+n3,  'Различие между группами статистически значимое' \
    if Fn > Fcrit else 'Различие между группами статистически не значимое')

y1_mean = np.mean(y1)
y2_mean = np.mean(y2)
y3_mean = np.mean(y3)
print(y1_mean, y2_mean, y3_mean)
y_all = np.concatenate([y1, y2, y3])
y_mean = np.mean(y_all)
s2 = np.sum((y_all - y_mean)**2)  # сумма квадратов отклонений
s2_f = ((y1_mean - y_mean)**2) * n1 + ((y2_mean - y_mean)**2) * n2 + ((y3_mean - y_mean)**2) * n3  # сумму квадратов \
# отклонений средних групповых значений от общего среднего

# y1 = np.array([70, 50, 65, 60, 75], dtype=np.float64)
# y2 = np.array([80, 75, 90, 70, 75, 65, 85, 100], dtype=np.float64)
# y3 = np.array([130, 100, 140, 150, 160, 170, 200], dtype=np.float64)
# y1_mean = np.mean(y1)
# y2_mean = np.mean(y2)
# y3_mean = np.mean(y3)
s2_res = np.sum((y1 - y1_mean)**2) + np.sum((y2 - y2_mean)**2) + np.sum((y3 - y3_mean)**2)  #  остаточная сумма \
# квадратов отклонений
print(s2_res)
print(s2_f + s2_res, s2)