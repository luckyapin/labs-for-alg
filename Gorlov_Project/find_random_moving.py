import matplotlib.pyplot as plt
import numpy as np
import random

from Exponential_smoothing import *
from moving_average import *
from UKF import *
from ERF import *


dx=0.1
x=np.arange(-20, 20, dx)
d=0.2
r=0.99
en=lambda i: 0.1
window_len=3

y = [random.normalvariate(0, 1)]
for i in range(1,len(x)):
    y.append(r*y[i-1] + random.normalvariate(0, en(0)))
y1=[i + random.normalvariate(0, d) for i in y]



ye = exponential_smoothing(y1, 0.4)
ym = moving_average(y1, window_len)
yu = UKF(y1, d, r, en)

print(erf(y, ye))
print(erf(y[window_len:-window_len], ym))
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
plt.plot(x[window_len:-window_len],ym)
plt.title('Скользящее среднее')
plt.grid(True)

sp = plt.subplot(224)
plt.plot(x, y1)
plt.plot(x, yu)
plt.title('фильтр Калмана')
plt.grid(True)

plt.show()
