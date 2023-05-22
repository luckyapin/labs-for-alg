def filter(data, alpha):
    ema = []
    for i in range(len(data)):
        if i == 0:
            ema.append(data[i])
        else:
            ema.append(alpha * data[i] + (1 - alpha) * ema[i-1])
    return ema


print(filter([1, 2, 3, 4, 5],0.7))
print(filter([1, 2, 3, 4, 5],0.0))
print(filter([1, 2, 3, 4, 5],1.0))
