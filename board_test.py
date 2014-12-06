import unittest
from board import Board


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.b = Board(9)
        
    def test_all_like(self):
        a = [1, 2, 3, 4]
        b = [1, 1, 1, 1]
        self.assertTrue(self.b.all_like(b, 1))
        self.assertFalse(self.b.all_like(a, 3))

    def test_is_free(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertTrue(self.b.is_free(0))
        self.assertFalse(self.b.is_free(1))
        self.assertFalse(self.b.is_free(2))

    def test_prepare_for_print(self):
        self.b.moves = [' ', 'X', 'O', ' ', 'X', 'O']
        self.assertEqual(self.b.prepare_for_print(),
                         [[' ', 'X', 'O'], [' ', 'X', 'O']])

    def test_is_winner_top_row_should_be_true(self):
        self.b.moves = ['X', 'X', 'X',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ']
        self.assertTrue(self.b.check_winning('X'))

    def test_is_winner_top_row_should_be_false(self):
        self.b.moves = ['X', 'O', 'X',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ']
        self.assertFalse(self.b.check_winning('X'))

    def test_is_winner_middle_row_should_be_true(self):
        self.b.moves = [' ', ' ', ' ',
                        'X', 'X', 'X',
                        ' ', ' ', ' ']
        self.assertTrue(self.b.check_winning('X'))

    def test_is_winning_middle_row_should_be_false(self):
        self.b.moves = [' ', ' ', ' ',
                        'O', 'X', 'X',
                        ' ', ' ', ' ']
        self.assertFalse(self.b.check_winning('X'))

    def test_is_winning_bottom_row_should_be_true(self):
        self.b.moves = [' ', ' ', ' ',
                        ' ', ' ', ' ',
                        'X', 'X', 'X']
        self.assertTrue(self.b.check_winning('X'))

    def test_is_winning_bottom_row_should_be_false(self):
        self.b.moves = [' ', ' ', ' ',
                        ' ', ' ', ' ',
                        'X', 'X', 'O']
        self.assertFalse(self.b.check_winning('X'))

    def test_is_winning_diagonals_should_be_true(self):
        self.b.moves = ['X', ' ', ' ',
                        ' ', 'X', ' ',
                        ' ', ' ', 'X']
        self.assertTrue(self.b.check_winning('X'))

        self.b.moves = [' ', ' ', 'X',
                        ' ', 'X', ' ',
                        'X', ' ', ' ']
        self.assertTrue(self.b.check_winning('X'))

    def test_is_winning_diagonals_should_be_false(self):
        self.b.moves = ['X', ' ', ' ',
                        ' ', 'O', ' ',
                        ' ', ' ', 'X']
        self.assertFalse(self.b.check_winning('X'))

        self.b.moves = [' ', ' ', 'X',
                        ' ', 'X', ' ',
                        'O', ' ', ' ']
        self.assertFalse(self.b.check_winning('X'))

    def test_is_valid_move_should_be_true(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertTrue(self.b.is_valid_move(0))

    def test_is_valid_move_should_be_false(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertFalse(self.b.is_valid_move(1))
        self.assertFalse(self.b.is_valid_move(2))

    def test_is_full_should_be_false(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertFalse(self.b.is_full())

    def test_is_full_should_be_true(self):
        self.b.moves = ['X', 'X', 'O']
        self.assertTrue(self.b.is_full())

    def test_make_move_should_be_true(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertTrue(self.b.make_move(0, 'X'))
        self.assertEqual(self.b.moves[0], 'X')

    def test_make_move_should_be_false(self):
        self.b.moves = [' ', 'X', 'O']
        self.assertFalse(self.b.make_move(1, 'O'))
        self.assertEqual(self.b.moves[1], 'X')

    def test_possible_moves(self):
        self.b.moves = [' ', 'X', 'O',
                        'O', 'X', 'O',
                        'X', 'X', 'O']
        self.assertEqual(self.b.possible_moves(), [0])


if __name__ == '__main__':
    unittest.main()
