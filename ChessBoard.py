import matplotlib.pyplot as plt
import matplotlib.patches as patches


class ChessBoard:
    def __init__(self, size):
        self.size = size
        self.board = [[False for i in range(size)] for j in range(size)]
        self.results = []

    def print_solutions(self):
        for i, solution in enumerate(self.results):
            print("Solution ", i + 1)
            self.print_board(solution)

    def print_board(self, solution):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        ax.set_xlim((1, self.size + 1))
        ax.set_ylim((0, self.size))

        count = 1
        for queen in solution:
            rectangle = patches.Rectangle((queen, self.size - count), 1, 1, color='Green')
            ax.add_patch(rectangle)
            rx, ry = rectangle.get_xy()
            cx = rx + rectangle.get_width() / 2.0
            cy = ry + rectangle.get_height() / 2.0
            ax.annotate("Q", (cx, cy), color='White', weight='bold', fontsize=10, ha='center', va='center')
            count += 1
        plt.show()
        plt.close(fig)

    # Check if it is safe to place a queen in this row and column.
    def checkSafe(self, row, column):
        return not (self.leftViolation(row, column) or
                    self.upperLeftViolation(row, column) or
                    self.lowerLeftViolation(row, column))

    # Check if there are queens already placed to the left.
    def leftViolation(self, row, column):
        for i in range(column):
            if self.board[row][i]:
                return True

    # Check if there are queens placed in the diagonal upper left.
    def upperLeftViolation(self, row, column):
        for r, c in zip(range(row, -1, -1), range(column, -1, -1)):
            if self.board[r][c]:
                return True

    # Check if there are queens placed to the lower diagonal left.
    def lowerLeftViolation(self, row, column):
        for r, c in zip(range(row, self.size, 1), range(column, -1, -1)):
            if self.board[r][c]:
                return True

    def solveNQueens(self, column):
        # If column == N means the last queen has been placed successfully.
        if column == self.size:
            temp = []
            # Iterate through the board, if variable is set to True, append column index + 1 to the result list.
            for i in self.board:
                for j in range(len(i)):
                    if i[j]:
                        temp.append(j + 1)
            self.results.append(temp)
            return True

        # If current column is < N, means we don't have a result yet.
        res = False

        # For each remaining row, check if it safe to place a queen there.
        # If it is, we set that place to True and move on to the next column.
        # If it is not, we set that place to False. This will lead to backtracking, we will go back a column,
        # function will try again with the next row, and the problem will continue to be solved until all possibilities
        # have been exhausted.

        for row in range(self.size):
            if self.checkSafe(row, column):
                self.board[row][column] = True

                res = self.solveNQueens(column + 1) or res

                self.board[row][column] = False

        return res

    def solve_N_queens(self):
        self.solveNQueens(0)
        self.print_solutions()
