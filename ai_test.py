import unittest
from ai import Ai
from board import Board


class AiTest(unittest.TestCase):
    def setUp(self):
        self.ai = Ai()
        self.b = Board(9)

    def test_make_winning_move(self):
        self.b.moves = [' ', 'X', 'O',
                        ' ', 'O', 'X',
                        ' ', 'X', ' ']
        self.assertEqual(self.ai.make_winning_move(self.b), 6)

    def test_block_move(self):
        self.b.moves = [' ', 'X', 'X',
                        ' ', 'O', 'X',
                        ' ', 'X', 'O']
        self.assertEqual(self.ai.block_move(self.b), 0)

    def test_should_win_instead_of_block(self):
        self.b.moves = ['X', ' ', 'X',
                        'O', 'O', ' ',
                        ' ', ' ', ' ']
        self.assertEqual(self.ai.get_ai_move(self.b), 5)

    def test_get_corner(self):
        self.b.moves = ['X', ' ', 'X',
                        ' ', ' ', ' ',
                        'X', ' ', 'X']
        self.assertIsNone(self.ai.move_corner(self.b))
        self.b.moves = ['X', ' ', ' ',
                        ' ', ' ', ' ',
                        'X', ' ', 'X']
        self.assertEqual(self.ai.move_corner(self.b), 2)
        self.b.moves = [' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ']
        result = []
        for i in range(100):
            result.append(self.ai.move_corner(self.b))
        self.assertIn(0, result)
        self.assertIn(2, result)
        self.assertIn(6, result)
        self.assertIn(8, result)

    def test_move_middle(self):
        self.b.moves = ['X', ' ', 'X',
                        'O', ' ', ' ',
                        'X', ' ', 'X']
        self.assertEqual(self.ai.move_middle(self.b), 4)
        self.b.moves = [' ', ' ', ' ',
                        ' ', 'X', ' ',
                        ' ', ' ', ' ']
        self.assertIsNone(self.ai.move_middle(self.b))

    def test_move_side(self):
        self.b.moves = [' ', 'O', ' ',
                        'O', ' ', 'O',
                        ' ', 'O', ' ']
        self.assertIsNone(self.ai.move_side(self.b))
        self.b.moves = [' ', 'O', ' ',
                        ' ', ' ', 'O',
                        ' ', 'O', ' ']
        self.assertEqual(self.ai.move_side(self.b), 3)
        self.b.moves = [' ', ' ', ' ',
                        ' ', ' ', ' ',
                        ' ', ' ', ' ']
        result = []
        for i in range(100):
            result.append(self.ai.move_side(self.b))
        self.assertIn(1, result)
        self.assertIn(3, result)
        self.assertIn(5, result)
        self.assertIn(7, result)

        
        
if __name__ == '__main__':
    unittest.main()
