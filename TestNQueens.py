import unittest
from ChessBoard import ChessBoard


class MyTestCase(unittest.TestCase):

    def test_n_queens_1(self):
        board = ChessBoard(1)
        board.solve_N_queens()
        self.assertEqual(1, len(board.results))
        self.assertEqual([[1]], board.results)

    def test_n_queens_2(self):
        board = ChessBoard(2)
        board.solve_N_queens()
        self.assertEqual(0, len(board.results))

    def test_n_queens_3(self):
        board = ChessBoard(3)
        board.solve_N_queens()
        self.assertEqual(0, len(board.results))

    def test_n_queens_4(self):
        board = ChessBoard(4)
        board.solve_N_queens()
        self.assertEqual(2, len(board.results))
        self.assertEqual([[3, 1, 4, 2], [2, 4, 1, 3]], board.results)

    def test_n_queens_5(self):
        board = ChessBoard(5)
        board.solve_N_queens()
        self.assertEqual(10, len(board.results))
        self.assertEqual([[1, 4, 2, 5, 3],
                         [1, 3, 5, 2, 4],
                         [3, 1, 4, 2, 5],
                         [4, 1, 3, 5, 2],
                         [2, 4, 1, 3, 5],
                         [5, 3, 1, 4, 2],
                         [2, 5, 3, 1, 4],
                         [5, 2, 4, 1, 3],
                         [4, 2, 5, 3, 1],
                         [3, 5, 2, 4, 1]], board.results)


if __name__ == '__main__':
    unittest.main()
