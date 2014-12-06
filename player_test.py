import unittest
from player import Player
from board import Board


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.p = Player()
        self.b = Board(9)
        
    def test_is_input_valid(self):
        self.assertTrue(self.p.is_input_valid(2, self.b))
        self.assertFalse(self.p.is_input_valid(15, self.b))

    def test_move_to_index(self):
        self.assertEqual(self.p.move_to_index(2), 1)
        self.assertEqual(self.p.move_to_index(10), 9)

if __name__ == '__main__':
    unittest.main()
