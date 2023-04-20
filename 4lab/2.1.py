


def matrix(dims):
    n = len(dims) # вычисление длины

    # c[i, j] = минимальное количество скалярных умножений
    # требуется для вычисления матрицы `M[i] M[i+1] … M[j] = M[i…j]`
    # 0 - при умножении одной матрицы
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]

    print(c)
    for length in range(2, n + 1):  # Длина подпоследовательности
        for i in range(1, n - length + 2):
            print(i,length)
            j = i + length - 1
            c[i][j] = float('inf')
            k = i
            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                if cost < c[i][j]:
                    c[i][j] = cost

                k = k + 1

    return c[1][n - 1]


# матрица 10 × 20, матрица 20 × 5, матрица 5 × 60
dims = [2, 3, 1, 3]

print("Минимальное количество умножений:", matrix(dims))

