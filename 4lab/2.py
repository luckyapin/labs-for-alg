
def matrix(p):
    n = len(p) - 1 # кол-о матриц

    #заполняем нулями
    m = [[0 for x in range(n)] for y in range(n)]

    #начинаем перебор
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float('inf') # т.к. только ищем минимум

            #сдвигаем k, чтобы найти наиболее выгодный вариант
            for k in range(i, j):
                #разбиение + стоимост
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                #ищем минимум
                m[i][j] = min(q, m[i][j])
    return m

#матрицы 20 на 31, 31 на 11, 11 на 33, 33 на 21
p = [20, 31, 11, 33,21]
m = matrix(p)
print("Минимальное количество умножений:", m[0][-1])





