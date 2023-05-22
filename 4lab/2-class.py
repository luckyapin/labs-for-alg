

def split_array(A):
    n = len(A) # длина массив
    total_sum = sum(A) # вся сумма

    # иницилизация массива (для динамики) размером (n+1)*(sum+1)
    # хранит максимальную сумму элементов, которую можно получить из первых i элементов массива A суммой не более j
    dp = [[0 for _ in range(total_sum + 1)] for _ in range(n + 1)]

    # перебор
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if j < A[i - 1]:
                # значение dp[i][j] равно значению dp[i - 1][j] так как текущий
                # элемент не может быть включен в первый список
                dp[i][j] = dp[i - 1][j]
            else:
                # либо текущий элемент не входит в первый список - значение равно dp[i-1][j]
                # либо текущий элемент входит в первый список, и тогда значение равно dp[i-1][j-A[i-1]] + A[i-1]
                # также для одбора единичных элементов (пример для A=[2,1,3], появится 1)
                # при i=j=2 [[0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 2, 2, 2, 2], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

    # минимальная разница
    min_diff = total_sum - 2 * dp[n][total_sum // 2]

    A1 = []
    A2 = []
    j = total_sum // 2
    #восстановим A1 и A2
    # мы можем пройти по массиву в обратном порядке начиная с
    # dp[n][total_sum // 2] и добавлять элементы в первый список если
    # они входят в него или во второй список, если нет
    for i in range(n, 0, -1):
        if dp[i][j] == dp[i - 1][j]:
            A2.append(A[i - 1])
        else:
            A1.append(A[i - 1])
            j -= A[i - 1]

    return A1, A2, min_diff


# пример
A = [2, 1, 4, 2, 3, 5,2,3,5]
A1, A2, min_diff = split_array(A)
print("A1 -", A1,"Сумма -",sum(A1))
print("A2 -", A2,"Сумма -",sum(A2))
print("Разница -",min_diff)


