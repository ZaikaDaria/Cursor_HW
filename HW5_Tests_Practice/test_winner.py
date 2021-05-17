import unittest
from game import TicTacToe

class TestWinner(unittest.TestCase):


    def setUp(self):
        self.board = TicTacToe()

    def test_check_column_win(self):
        self.board.rows = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.board.winner(6, ' '))

    def test_check_row_win(self):
        self.board.rows = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.board.winner(6, ' '))

    def test_check_first_diagonal_win(self):
        self.board.rows = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(self.board.winner(6, ' '))

    def test_check_second_diagonal_win(self):
        self.board.rows = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        self.assertTrue(self.board.winner(6, ' '))


if __name__ == '__main__':
    unittest.main()