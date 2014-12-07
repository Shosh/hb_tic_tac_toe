from copy import deepcopy


class Player():
    def __init__(self):
        self.symbol = 'X'

    def ask_for_move(self, board):
        human_input = input('Your move: ')
        
        try:
            human_input = int(human_input)
        except ValueError:
            return self.ask_for_move(board)
        if self.is_input_valid(human_input, board):
            return self.move_to_index(human_input)
        else:
            return self.ask_for_move(board)
            
    def is_input_valid(self, inp, board):
        pm = board.possible_moves()
        if inp - 1 not in pm:
            return False
        else:
            return True

    def move_to_index(self, move):
        return move - 1

    def show_possible_moves(self, board):
        pm = board.possible_moves()
        cb = deepcopy(board)
        for index in pm:
            cb.moves[index] = index + 1
        # returns smthing like --- --- --- \n | 1 | 2 | 3 | \n and so on
        intro = 'Just pick one: \n'
        return intro + cb.draw()
        
