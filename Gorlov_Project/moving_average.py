def moving_average(x, window_len):
    y = []
    window_sum = sum(x[:window_len*2+1])
    for i in range(window_len, len(x) - window_len):
        y.append(window_sum/(window_len * 2 + 1))
        window_sum += x[window_len+i] - x[i-window_len]
    return y


