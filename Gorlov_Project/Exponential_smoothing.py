def exponential_smoothing(x,a):
    y=[x[0]]
    for i in range(1,len(x)):
        y.append(a * x[i] + (1-a) * y[i-1])
    return y

