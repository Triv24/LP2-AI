class Node:
    def __init__(self, board, row, g_cost):
        self.board = board          
        self.row = row             
        self.g = g_cost            
        self.h = self.heuristic()   
        self.f = self.g + self.h    
      
    def heuristic(self):
        attacks = 0
        n = len(self.board)
        positions = []

        for i in range(n):
            for j in range(n):
                if self.board[i][j] == 1:
                    positions.append((i, j))

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                if c1 == c2:
                    attacks += 1
                if abs(r1 - r2) == abs(c1 - c2):
                    attacks += 1
        return attacks


def isSafe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def AStar_NQueen(n):
    open_list = []
    board = [[0 for i in range(n)] for j in range(n)]
    start = Node(board, 0, 0)
    open_list.append(start)

    while open_list:
        open_list.sort(key=lambda x: x.f)
        current = open_list.pop(0)

        if current.row == n and current.h == 0:
            return current.board

        if current.row < n:
            for col in range(n):
                if isSafe(current.board, current.row, col, n):
                    new_board = [r[:] for r in current.board]
                    new_board[current.row][col] = 1
                    child = Node(new_board,
                                 current.row + 1,
                                 current.g + 1)
                    open_list.append(child)
    return None

def printBoard(board, n):
    print("\nSolution Board:\n")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def main():
    n = int(input("Enter number of Queens: "))
    solution = AStar_NQueen(n)
    if solution:
        printBoard(solution, n)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
