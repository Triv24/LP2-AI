# BACKTRACKING
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_bt(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens_bt(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Driver code
n = int(input("Enter the value of n : "))
board = [[0]*n for _ in range(n)]

print("Backtracking Solution:")
solve_n_queens_bt(board, 0, n)

# BRANCH AND BOUND

def print_solution(positions, n):
    board = [["." for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i][positions[i]] = "Q"

    for row in board:
        print(" ".join(row))
    print()


def solve_n_queens_bb(n):
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    positions = [-1] * n

    def solve(row):
        if row == n:
            print_solution(positions, n)
            return True

        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n]:
                
                positions[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n] = True

                if solve(row + 1):
                    return True

                # Backtrack
                positions[row] = -1
                cols[col] = diag1[row + col] = diag2[row - col + n] = False

        return False

    solve(0)


# Driver code
n = int(input("Enter the value of n : "))
print("Branch and Bound Solution:")
solve_n_queens_bb(n)
