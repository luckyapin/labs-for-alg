def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    for row in board:
        for cell in row:
            print("Q" if cell == 1 else ".", end=" ")
        print()
    print("\n")


def solve_n_queens(board, row):
    if row == len(board):
        print_board(board)
        return 1
    count = 0
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            count += solve_n_queens(board, row+1)
            board[row][col] = 0
    return count


def count_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    return solve_n_queens(board, 0)


if __name__ == "__main__":
    n = 8
    print("Число возможных расстановок для {} ферзей: {}".format(n, count_n_queens(n)))

