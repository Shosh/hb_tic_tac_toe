from ai import Ai
from board import Board
from player import Player


class Game():
    def __init__(self):
        self.ai = Ai()
        self.board = Board(9)
        self.player = Player()
        self.on_turn = self.player
   
    def start(self):
        in_progres = True
        while in_progres:
            if self.on_turn == self.player:
                player_choice = self.player.ask_for_move(self.board)
                try:
                    self.board.make_move(player_choice, self.player.symbol)
                except ValueError:
                    self.player.ask_for_move(self.board)
                self.on_turn = self.ai
                print(self.board.draw())
            else:
                print('Ai move:')
                ai_move = self.ai.get_ai_move(self.board)
                self.board.make_move(ai_move, self.ai.symbol)
                self.on_turn = self.player
                
                print(self.board.draw())

            if self.board.check_winning(self.player.symbol):
                print('Congrats, You win!!!')
                break
            elif self.board.check_winning(self.ai.symbol):
                print('You are LOOOOOOOOOOSER :P')
                break
            elif self.board.is_full():
                print('TIE')
                
            in_progres = not self.board.is_full()
            
            
            













