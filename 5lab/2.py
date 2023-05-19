from random import randint

#создаем матрицу
M = 3
N = 5
a = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        while True:
            k = randint(1, M*N*2)
            if k not in [x for row in a for x in row]:
                a[i][j] = k
                break
    a[i].sort()
a.sort()


for row in a:
    print(row)

element = int(input())

#бинарный поиск
def search_matrix(matrix, value):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        mid = len(matrix[i]) // 2
        low = 0
        high = len(matrix[i]) - 1
        while a[i][mid] != value and low <= high:
            if value > a[i][mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        if low > high:
            if i==m-1:
                return("No value")
        else:
            return f"ID = {i, mid}"

print(search_matrix(a,element))


