import sys

def is_valid(board, row, col, n):
    # Check if a queen can be placed at row, col
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row, n):
    # Base case: all rows have a queen
    if row == n:
        print(' '.join(str(col + 1) for col in board))
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            solve(board[:], row + 1, n)

def nqueens(n):
    # Check the input argument
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    board = [-1] * n
    solve(board, 0, n)

if __name__ == '__main__':
    # Parse the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
