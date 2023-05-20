from random import randint

start = 0
def generate():
    global start
    start += randint(1, 10)
    return start

M, N = (randint(3, 20) for _ in range(2))
matrix = [[generate() for _ in range(N)] for _ in range(M)]

def binary_search_matrix(x):
    global M, N, matrix
    l, rest = 0, M * N
    while rest > 0:
        guess, step = l + rest//2, rest//2
        if matrix[guess//N][guess%N] < x:
            guess += 1
            l = guess
            rest -= step + 1
        else:
            rest = step
    if l < M * N and matrix[l//N][l%N] == x:
        return l//N, l%N
    else:
        return "No element"

if __name__ == "__main__":
    el = randint(1, 1_000)

    tabulation_value = int(max(max(len(str(e)) for e in row) for row in matrix) + 1)
    pretty_matrix = lambda m: '\n'.join(''.join(str(e) + ' '*(tabulation_value - len(str(e))) for e in row) for row in m)
    print(f'\nSearching element {el} in matrix:\n{pretty_matrix(matrix)}\n'
          f'\nPosition of element: {binary_search_matrix(el)}\n')