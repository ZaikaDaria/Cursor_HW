import unittest
from game import TicTacToe

class TestWinner(unittest.TestCase):


    def setUp(self):
        self.game = TicTacToe()

    def test_check_column_win(self):
        self.game.board = [['X', 'X', 'X'], [' ', 'O', ' '], [' ', ' ', ' ']]
        self.assertTrue(self.game.winner(6, 'X'))

    def test_check_row_win(self):
        self.game.board = ['X', 'X', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(0, 'X'))

    def test_check_first_diagonal_win(self):
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(2, 'X'))

    def test_check_second_diagonal_win(self):
        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.assertFalse(self.game.winner(5, 'X'))


if __name__ == '__main__':
    unittest.main()