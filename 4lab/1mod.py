
def max_expression(A):
    n = len(A)
    dp = [[0] * n for _ in range(4)]

    A = list(reversed(A))

    # вычисляем значения на префиксах
    dp[0][0] = A[0]
    dp[1][0] = float("-inf")
    dp[2][0] = float("-inf")
    dp[3][0] = float("-inf")

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], A[i])
        dp[1][i] = max(dp[1][i-1], dp[0][i-1] - A[i])
        dp[2][i] = max(dp[2][i-1], dp[1][i-1] + A[i])
        dp[3][i] = max(dp[3][i-1], dp[2][i-1] - A[i])

    return dp[3][-1]

A = [1, 3, 5, 6, 2, 4] #4-2+6-1=7
print(max_expression(A))

array = [7, 2, 6, 4, 1, 5, 3, 8] #8-1+6-2=11
print(max_expression(array))