def filter(data, alpha):
    ema = [data[0]]
    for i in range(1, len(data)):
        ema.append(ema[i - 1] + alpha* (data[i] - ema[i - 1]))
    return ema
print(filter([1, 2, 3, 4, 5], 0.7))
print(filter([1, 2, 3, 4, 5], 0.0))
print(filter([1, 2, 3, 4, 5], 1.0))

