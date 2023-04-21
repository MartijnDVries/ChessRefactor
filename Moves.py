from config import *
from CheckForChecks import CheckForChecks
from SquareTable import SquareTable
from Singleton import Singleton
import ujson

class LegalMoves(metaclass=Singleton):
    def __init__(self):
        self.check = CheckForChecks()
        self.tableClass = SquareTable()
        self.moves = []

    def is_legal(self, old_square, new_square, piece_name):
        move = f"{old_square}:{new_square}"
        # if move in self.moves_list()
        return True

    
    def copy(self, table):
        return ujson.loads(ujson.dumps(table))

    def moves_list(self, table, own_color):
        moves_list = []
        for square in table:
            if table[square][COLOR] == own_color.upper():
                if table[square][PIECENAME] == "ROOK":
                    for dir in ["right", "left"]:
                      squares = self.check.horizontal_squares_from(square, dir)
                      moves_list.extend(self.rook_moves(table, square, squares, own_color))
                    for dir in ["up", "down"]:
                      squares = self.check.horizontal_squares_from(square, dir)
                      moves_list.extend(self.rook_moves(table, square, squares, own_color))
                elif table[square][PIECENAME] == "PAWN":
                    moves_list.extend(self.pawn_moves(table, square))

    def rook_moves(self, table, rook_square, squares, own_color):
        moves = []
        for square in squares:
            if table[square][PIECENAME] and table[square][COLOR] == own_color:
                return moves
            if table[square][PIECENAME] and table[square][COLOR] != own_color:
                table_copy = self.copy(table)
                self.tableClass.setStaticMove(rook_square, square, table_copy)
                if not(self.check.is_in_check(own_color, table_copy)):
                    moves.append(f"{rook_square}:{square}")
            elif not table[square][PIECENAME]:
                table_copy = self.copy(table)
                self.tableClass.setStaticMove(rook_square, square, table_copy)
                if not(self.check.is_in_check(own_color, table_copy)):
                    moves.append(f"{rook_square}:{square}")
                                
    def pawn_moves(self, table, pawn_square, own_color):
        if self.possible_en_passant():
            pass
        
    def possible_en_passant(self):
        pass
        
    
                    
if __name__ == "__main__":
    pass

