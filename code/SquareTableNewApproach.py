from Singleton import Singleton
from config import *
import ujson
from start_position import StartPos
from Coordinates import Coordinates
import timeit
import numpy as np

class SquareTableNewApproach(metaclass=Singleton):
    """Create a Table of the squares of the board which contain information about the status of the board at any given moment"""


    def __init__(self):
        self.squareTableNumpy = StartPos().startposNumpy
        self.coordinates = Coordinates().coordinates
        self.square_index_list = [(file + str(row)) for row in range(1, 9) for file in 'abcdefgh']


    def getSquareIndex(self, square):
        return self.square_index_list.index(square)


    def getSquareFromIndex(self, index):
        return self.square_index_list[index]


    def getTable(self):
        return self.squareTableNumpy


    def getRow(self, square_index):


        return f'\n\
        SQUARE: {self.getSquareFromIndex(square_index)}\n\
        COLOR: {self.squareTableNumpy[square_index][COLOR]}\n\
        PIECE: {self.squareTableNumpy[square_index][PIECENAME]}\n'


    def getPositionFromSquare(self, square):
        return self.coordinates[square]


    def getSquareFromPos(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]

        index = list(filter(lambda s: self.coordinates[s][0] 
            in range( pos_x - (SQUAREWIDTH//2), pos_x + (SQUAREWIDTH//2))
            and self.coordinates[s][1] in range(pos_y - (SQUAREHEIGHT//2), pos_y + ((SQUAREHEIGHT//2))), 
            self.coordinates))
        
        return self.getSquareFromIndex(index[0])


    def getSquareFromPiece(self, piece_name, piece_color, table=None):
        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy

        # index = list(filter(lambda s: table[s][PIECENAME] == piece_name.upper()
        #                      and table[s][COLOR] == piece_color.upper(), table))
        index = 0
        for square in table:
            if square[PIECENAME] == piece_name.upper() \
                    and square[COLOR] == piece_color.upper():
                return index
            index += 1
        return "Piece not found"
        
        # return [self.getSquareFromIndex(index[0])]

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

    def setEnpassantMove(self, enemy_pawn_square_index, new_square_index, old_square_index, table=None):

        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy

        table[new_square_index][COLOR] = table[old_square_index][COLOR]
        table[new_square_index][PIECENAME] = table[old_square_index][PIECENAME]
        self.emptySquare(old_square_index, table)
        self.emptySquare(enemy_pawn_square_index, table)


    def castle(self, color, side, table=None):
        
        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy

        if color == "WHITE":
          if side == "king_side":
              self.setMove(E1, G1, table)
              self.setMove(H1, F1, table)
          elif side == "queen_side":
              self.setMove(E1, C1, table)
              self.setMove(A1, D1, table)
        elif color == "BLACK":
            if side == "king_side":
                self.setMove(E8, G8, table)
                self.setMove(H8, F8, table)
            elif side == "queen_side":
                self.setMove(E8, C8, table)
                self.setMove(A8, D8, table)


    def setMove(self, old_square_index, new_square_index, table=None):
        print(f"OLD SQI: {old_square_index}, NSQI: {new_square_index}")
        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy

        table[new_square_index] = table[old_square_index]
        self.emptySquare(old_square_index, table)


    def emptySquare(self, square_index, table=None):

        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy

        table[square_index][COLOR] = ""
        table[square_index][PIECENAME] = ""


    def hasPiece(self, square, piece=None):
        if piece:
            return square[PIECENAME] == piece
        else:
            return square[PIECENAME] != ""
        
    def hasColor(self, square, color):
        return square[COLOR] == color


    def print(self, square):
        print(self.getRow(square))


    


    def printTable(self, table=None):
        if not isinstance(table, np.ndarray):
            table = self.squareTableNumpy
        index = 0
        for values in table:
            print(f"{self.getSquareFromIndex(index)}: {values}")
            index += 1


    @staticmethod
    def copyTable(array):
        return np.copy(array)


if __name__ == "__main__":
    s = SquareTableNewApproach()
    # print(s.getRow('a1'))
    # print(timeit.timeit('s.copy(s.squareTable)', 'from __main__ import s', number=1000000))

    # print(s.getSquareFromPiece('KING', 'WHITE'))

    s.setMove(E1, E5)

    s.printTable()
