from Singleton import Singleton
from config import *
import ujson
from start_position import StartPos
from Coordinates import Coordinates
import timeit
import numpy as np

class SquareTable(metaclass=Singleton):
    """Create a Table of the squares of the board which contain information about the status of the board at any given moment"""

    def __init__(self):
        self.squareTable = StartPos().startpos
        self.squareTableNumpy = StartPos().startposNumpy
        self.coordinates = Coordinates().coordinates
        
    def __str__(self):
        for k, v in self.__dict__.items():
            for square, values in v.items():
                return f"{square}: {values}"

    def getTable(self):
        return self.squareTable

    def getRow(self, square):
        return f'\n\
        SQUARE: {square}\n\
        COLOR: {self.squareTable[square][COLOR]}\n\
        PIECE: {self.squareTable[square][PIECENAME]}\n'

    def getPositionFromSquare(self, square):
        return self.coordinates[square]

    def getSquareFromPos(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        square = list(filter(lambda s: self.coordinates[s][0] 
            in range( pos_x - (SQUAREWIDTH//2), pos_x + (SQUAREWIDTH//2))
            and self.coordinates[s][1] in range(pos_y - (SQUAREHEIGHT//2), pos_y + ((SQUAREHEIGHT//2))), 
            self.coordinates))
        return square[0]

    @staticmethod
    def getSquareFromPiece(piece_name, piece_color, table):
        square = list(filter(lambda s: table[s][PIECENAME] == piece_name.upper()
                             and table[s][COLOR] == piece_color.upper(), table))
        
        return square

    # @staticmethod
    # def setStaticMove(old_square, new_square, table):
    #     table[new_square][COLOR] = table[old_square][COLOR]
    #     table[new_square][PIECENAME] = table[old_square][PIECENAME]
    #     SquareTable.emptyStaticSquare(old_square, table)
    #     return table

    # @staticmethod
    # def emptyStaticSquare(square, table):
    #     table[square][COLOR] = ""
    #     table[square][PIECENAME] = ""

    def setEnpassantMove(self, enemy_pawn_square, new_square, old_square, table=None):
        if not table:
            table = self.squareTable
        table[new_square][COLOR] = table[old_square][COLOR]
        table[new_square][PIECENAME] = table[old_square][PIECENAME]
        self.emptySquare(old_square, table)
        self.emptySquare(enemy_pawn_square, table)

    def castle(self, color, side, table=None):
        if not table:
            table = self.squareTable
        if color == "WHITE":
          if side == "king_side":
              self.setMove('e1', 'g1', table)
              self.setMove('h1', 'f1', table)
          elif side == "queen_side":
              self.setMove('e1', 'c1', table)
              self.setMove('a1', 'd1', table)
        elif color == "BLACK":
            if side == "king_side":
                self.setMove('e8', 'g8', table)
                self.setMove('h8', 'f8', table)
            elif side == "queen_side":
                self.setMove('e8', 'c8', table)
                self.setMove('a8', 'd8', table)

    def setMove(self, old_square, new_square, table=None):
        if not table:
            table = self.squareTable
        table[new_square][COLOR] = table[old_square][COLOR]
        table[new_square][PIECENAME] = table[old_square][PIECENAME]
        self.emptySquare(old_square, table)

    def emptySquare(self, square, table=None):
        if not table:
            table = self.squareTable
        table[square][COLOR] = ""
        table[square][PIECENAME] = ""

    def hasPiece(self, square, piece=None, table=None):
        if not table:
            table = self.squareTable
        if piece:
            return table[square][PIECENAME] == piece
        else:
            return table[square][PIECENAME] != ""

    def hasColor(self, square, color, table=None):
        if not table:
            table = self.squareTable
        return table[square][COLOR] == color

    def print(self, square):
        print(self.getRow(square))

    def printTable(self, table=None):
        if not table:
            table = self.squareTable
        for square, values in table.items():
            print(f"{square}: {values[1:]}")


    def copyTable(self, table):
        return ujson.loads(ujson.dumps(table))
    

    def copyNumpyTable(self, array):
        return np.copy(array)


if __name__ == "__main__":
    s = SquareTable()

    # print(timeit.timeit('s.copyTable(s.squareTable)', 'from __main__ import s', number=100000))

    # print(timeit.timeit('s.copyNumpyTable(s.squareTableNumpy)', 'from __main__ import s', number=100000))

    print(s.squareTable)