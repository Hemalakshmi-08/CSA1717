# Classic 8-Queens problem using backtracking

N = 8  # size of board and number of queens


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe
    given the current partial board.
    board[i] = column of queen in row i
    """
    for i in range(row):
        # same column
        if board[i] == col:
            return False
        # same diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(n=N):
    solutions = []

    def backtrack(board, row):
        if row == n:
            # found a full valid placement
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # reset (backtrack)

    backtrack([-1] * n, 0)
    return solutions


def print_board(solution):
    n = len(solution)
    for r in range(n):
        line = ""
        for c in range(n):
            line += "Q " if solution[r] == c else ". "
        print(line)
    print("-" * (2 * n))


if __name__ == "__main__":
    sols = solve_n_queens()
    print(f"Total solutions: {len(sols)}")
    print("First solution:")
    print_board(sols[0])
