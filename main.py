# Helper function to print the board.
# Receiving an array like [3, 1, 4, 2] it will output
# .  .  Q  .
# Q  .  .  .
# .  .  .  Q
# .  Q  .  .
# Where each . is a blank space, and each Q is a queen placed on the chessboard.

def printBoard(result):
    curr_index = 0
    for i in range(N):
        no_match_yet = True
        for j in range(N):
            if curr_index < N and result[curr_index] == j + 1 and no_match_yet:
                print(" Q ", end="")
                curr_index += 1
                no_match_yet = False
            else:
                print(" . ", end="")
        print("")


# Check if it is safe to place a queen in this row and column.
def checkSafe(board, row, column):
    return not (leftViolation(board, row, column) or
                upperLeftViolation(board, row, column) or
                lowerLeftViolation(board, row, column))


# Check if there are queens already placed to the left.
def leftViolation(board, row, column):
    for i in range(column):
        if board[row][i]:
            return True


# Check if there are queens placed in the diagonal upper left.
def upperLeftViolation(board, row, column):
    for r, c in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[r][c]:
            return True


# Check if there are queens placed to the lower diagonal left.
def lowerLeftViolation(board, row, column):
    for r, c in zip(range(row, N, 1), range(column, -1, -1)):
        if board[r][c]:
            return True


def solveNQueens(board, column):
    # If column == N means the last queen has been placed successfully.
    if column == N:
        temp = []
        # Iterate through the board, if variable is set to True, append column index + 1 to the result list.
        for i in board:
            for j in range(len(i)):
                if i[j]:
                    temp.append(j + 1)
        results.append(temp)
        return True

    # If current column is < N, means we don't have a result yet.
    res = False

    # For each remaining row, check if it safe to place a queen there.
    # If it is, we set that place to True and move on to the next column.
    # If it is not, we set that place to False. This will lead to backtracking, we will go back a column,
    # function will try again with the next row, and the problem will continue to be solved until all possibilities
    # have been exhausted.

    for row in range(N):
        if checkSafe(board, row, column):
            board[row][column] = True

            res = solveNQueens(board, column + 1) or res

            board[row][column] = False

    return res


N = 4
results = []

if __name__ == '__main__':
    testBoard = [[False for i in range(N)] for j in range(N)]
    solveNQueens(testBoard, 0)
    print(results)

    for i, solution in enumerate(results):
        print("Solution ", i + 1)
        printBoard(solution)
