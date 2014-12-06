import random
from copy import deepcopy


class Ai():
    def __init__(self):
        self.symbol = 'O'
        self.player = 'X'

    def get_random(self, options_list):
        return random.choice(options_list)
    
    def make_winning_move(self, board):
        pm = board.possible_moves()
        for index in pm:
            copy_board = deepcopy(board)
            copy_board.make_move(index, self.symbol)
            if copy_board.check_winning(self.symbol):
                return index
        else:
            return None

    def block_move(self, board):
        pm = board.possible_moves()
        for index in pm:
            copy_board = deepcopy(board)
            copy_board.make_move(index, self.player)
            if copy_board.check_winning(self.player):
                return index
        else:
            return None

    def get_intersection(self, list_a, list_b):
        return list(set(list_a).intersection(list_b))

    def move_corner(self, board):
        free_moves = board.possible_moves()
        corners = board.get_corners()
        possible_moves = self.get_intersection(free_moves, corners)
        if possible_moves:
            return self.get_random(possible_moves)
        else:
            return None

    def move_middle(self, board):
        free_moves = board.possible_moves()
        middle = board.get_middle()
        possible_moves = self.get_intersection(free_moves, middle)
        if possible_moves:
            return possible_moves[0]
        else:
            return None

    def move_side(self, board):
        free_moves = board.possible_moves()
        sides = board.get_sides()
        possible_moves = self.get_intersection(free_moves, sides)
        if possible_moves:
            return self.get_random(possible_moves)
        else:
            return None
        
    def get_ai_move(self, board):
        move = self.make_winning_move(board)
        if move is None:
            move = self.block_move(board)
        if move is None:
            move = self.move_corner(board)
        if move is None:
            move = self.move_middle(board)
        if move is None:
            move = self.move_side(board)
        return move
