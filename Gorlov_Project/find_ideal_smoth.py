import matplotlib.pyplot as plt
import numpy as np
import random

from Exponential_smoothing import *
from moving_average import *
from UKF import *
from ERF import *

x=np.arange(-10, 10, 0.001)
d=0.2
r=1
en=lambda i: np.cos(x[i])*0.001*10

y = [np.sin(x[0])]
for i in range(1,len(x)):
    y.append(r*y[i-1] + np.cos(x[i])*0.001 )
y1=[i + random.normalvariate(0, d) for i in y]
ar=[]
for a in np.arange(0.036, 0.037, 0.000001):
    ar.append((erf(y, exponential_smoothing(y1, a)), a))
print(sorted(ar)[:5])