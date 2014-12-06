import unittest
from game import Game
from board import Board


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        # self.board = Board(9)

    def test_start(self):
        self.game.start()
    
if __name__ == '__main__':
    unittest.main()
