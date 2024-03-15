def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if board[i] == j:
            return False

    return True

def solve_queens_util(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens_util(board, row + 1):
                return True
            board[row] = -1  # backtrack

    return False

def solve_queens():
    board = [-1] * 8
    if not solve_queens_util(board, 0):
        print("No solution exists.")
    else:
        print("Solution:")
        for i in range(8):
            print(" -" * board[i] + " Q" + " -" * (7 - board[i]))

solve_queens()
