from Moves import LegalMoves
from SquareTable import SquareTable
from Singleton import Singleton


class Game(metaclass=Singleton):
    def __init__(self):
        self.legalMoves = LegalMoves()
        self.tableClass = SquareTable()
        self.table = self.tableClass.getTable()
        self.turn = "WHITE"
        self.create_moves_for(self.turn)
        self.move = 0

    def create_moves_for(self, color):
        self.legalMoves.moves_list(self.table, color)

    def setTurn(self):
        if self.turn == "WHITE":
            self.turn = "BLACK"
            return
        self.turn = "WHITE"

    def check_game_outcome(self):
        self.setTurn()
        self.create_moves_for(self.turn)
        print(self.legalMoves.moves)

    def fifty_move_rule(self):
        pass
    
