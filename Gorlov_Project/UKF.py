import numpy as np

def UKF(x, d, r, en):
    y = [x[0]]
    P = [d]
    for i in range(1, len(x)):
        Pe = r**2 * P[i-1] + (en(i))**2
        P.append((Pe * d) / (Pe + d))
        y.append(r * y[i-1] + P[i] / d * (x[i] - r * y[i-1]))
    return y

