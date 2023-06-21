import matplotlib.pyplot as plt
import numpy as np
import random

from Exponential_smoothing import *
from moving_average import *
from UKF import *
from ERF import *


dx=0.001
x=np.arange(-20, 20, dx)
d=0.2
r=1
en=lambda i: np.cos(x[i])*dx*10

y = [np.sin(x[0])]
for i in range(1,len(x)):
    y.append(r*y[i-1] + np.cos(x[i])*dx )
y1=[i + random.normalvariate(0, d) for i in y]



ye = exponential_smoothing(y1, 0.037)
ym = moving_average(y1, 50)
yu = UKF(y1, d, r, en)

print(erf(y, ye))
print(erf(y[50:-50], ym))
print(erf(y, yu))

sp = plt.subplot(221)
plt.plot(x, y1)
plt.plot(x, y)
plt.title('Оригинальный и с шумом')
plt.grid(True)

sp = plt.subplot(222)
plt.plot(x, y1)
plt.plot(x, ye)
plt.title('Экспонинциальное сглаживание')
plt.grid(True)

sp = plt.subplot(223)
plt.plot(x, y1)
plt.plot(x[50:-50],ym)
plt.title('Скользящее среднее')
plt.grid(True)

sp = plt.subplot(224)
plt.plot(x, y1)
plt.plot(x, yu)
plt.title('фильтр Калмана')
plt.grid(True)

plt.show()
