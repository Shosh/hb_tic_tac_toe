from copy import deepcopy


class Board():
    winning_rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # up and down
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # across
                    [0, 4, 8], [2, 4, 6]]             # diagonal
    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]
    middle = [4]
    
    def __init__(self, size):
        self.empty = ' '
        self.human = 'X'
        self.ai = 'O'
        self.moves = [self.empty] * size

    def set_board(self, number):
        self.moves = [[self.empty] * number]
        
    def get_corners(self):
        return deepcopy(Board.corners)

    def get_sides(self):
        return deepcopy(Board.sides)

    def get_middle(self):
        return deepcopy(Board.middle)

    def all_like(self, list, item):
        return all(result == item for result in list)

    def is_free(self, index):
        return self.moves[index] == self.empty

    def prepare_for_print(self):
        step = 3
        board = [self.moves[i: i + step]
                 for i in range(0, len(self.moves),
                                step)]
        return board

    def draw(self):
        board = self.prepare_for_print()
        result = ''
        for i in range(len(board) * 2 + 1):
            if i % 2 == 0:
                result += ' --- --- ---'
            else:
                result += '\n| {} | {} | {} |\n'.format(*board[i // 2])
        return result

    def check_winning(self, symbol):
        for row in Board.winning_rows:
            l = [self.moves[w_move] for w_move in row]
            if self.all_like(l, symbol):
                return True
        return False

    def is_valid_move(self, index):
        return self.moves[index] == self.empty

    def is_full(self):
        if self.empty not in self.moves:
            return True
        else:
            return False

    def make_move(self, index, symbol):
        board = deepcopy(self.moves)
        if self.is_free(index):
            board[index] = symbol
            self.moves = board
            return True
        else:
            return False

    def possible_moves(self):
        result = [x for x, y in enumerate(self.moves) if self.is_valid_move(x)]
        # for x, y in enumerate(self.moves):
        #     if self.is_valid_move(x):
        #         result.append(x)
        return result
