from Moves import LegalMoves
from SquareTable import SquareTable


class Game:
    def __init__(self):
        self.legalMoves = LegalMoves()
        self.tableClass = SquareTable()
        self.table = self.tableClass.getTable()
        self.turn = "WHITE"

    def create_moves_for(self, color):
        self.legalMoves.moves_list(self.table, color)

    def setTurn(self):
        if self.turn == "WHITE":
            self.turn = "BLACK"
            return
        self.turn = "WHITE"

    
    