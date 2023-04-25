
def split_array(A):
    n = len(A)
    total_sum = sum(A)
    dp = [[0 for _ in range(total_su m +1)] for _ in range( n +1)]

    for i in range(1, n+ 1):
        for j in range(1, total_sum + 1):
            if j < A[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])

    min_diff = total_sum - 2 * dp[n][total_sum // 2]

    A1 = []
    A2 = []
    j = total_sum // 2
    for i in range(n, 0, -1):
        if dp[i][j] == dp[i - 1][j]:
            A2.append(A[i - 1])
        else:
            A1.append(A[i - 1])
            j -= A[i - 1]

    return A1, A2


A = [1, 6, 11, 5]
A1, A2 = split_array(A)
print("A1:", A1)
print("A2:", A2)