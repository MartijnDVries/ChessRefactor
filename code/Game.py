from MovesNumpy import LegalMovesNumpy
from Position import Position
from Singleton import Singleton


class Game(metaclass=Singleton):
    def __init__(self):
        self.legalMoves = LegalMovesNumpy()
        self.positionHandler = Position()
        self.position = self.positionHandler.position
        self.turn = "WHITE"
        self.create_moves_for(self.turn)
        self.move = 0
        self.quit = True
        self.start = True

    def create_moves_for(self, color):
        moves = self.legalMoves.moves_list(self.position,  self.turn)
        print(moves)

    def setTurn(self):
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else:
            self.turn = "WHITE"

    def check_game_outcome(self):
        self.setTurn()
        self.create_moves_for(self.turn)

    def fifty_move_rule(self):
        pass
