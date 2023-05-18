from Singleton import Singleton
from config import *
from start_position import StartPos
from Coordinates import Coordinates
import timeit
import numpy as np

class Position(metaclass=Singleton):
    """Create a Table of the squares of the board which contain information about the status of the board at any given moment"""


    def __init__(self):
        self.position = StartPos().startpos
        self.coordinates = Coordinates().coordinates
        self.square_index_list = [(file + str(row)) for row in range(1, 9) for file in 'abcdefgh']


    def getSquareIndex(self, square):
        return self.square_index_list.index(square)


    def getSquareFromIndex(self, index):
        return self.square_index_list[index]


    def getTable(self):
        return self.position


    def getRow(self, square_index):
        return f'\n\
        SQUARE: {self.getSquareFromIndex(square_index)}\n\
        COLOR: {self.position[square_index][COLOR]}\n\
        PIECE: {self.position[square_index][PIECENAME]}\n'


    def getPositionFromSquare(self, square):
        return self.coordinates[square]


    def getSquareFromPos(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]

        index = list(filter(lambda s: self.coordinates[s][0] 
            in range( pos_x - (SQUAREWIDTH//2), pos_x + (SQUAREWIDTH//2))
            and self.coordinates[s][1] in range(pos_y - (SQUAREHEIGHT//2), pos_y + ((SQUAREHEIGHT//2))), 
            self.coordinates))
        
        return index[0]


    def getSquareFromPiece(self, piece_name, piece_color, position=None):
        if not isinstance(position, np.ndarray):
            position = self.position

        # index = list(filter(lambda s: position[s][PIECENAME] == piece_name.upper()
        #                      and position[s][COLOR] == piece_color.upper(), position))
        index = 0
        for square in position:
            if square[PIECENAME] == piece_name.upper() \
                    and square[COLOR] == piece_color.upper():
                return index
            index += 1
        return "Piece not found"
        
        # return [self.getSquareFromIndex(index[0])]

    # @staticmethod
    # def setStaticMove(old_square, new_square, position):
    #     position[new_square][COLOR] = position[old_square][COLOR]
    #     position[new_square][PIECENAME] = position[old_square][PIECENAME]
    #     SquareTable.emptyStaticSquare(old_square, position)
    #     return position

    # @staticmethod
    # def emptyStaticSquare(square, position):
    #     position[square][COLOR] = ""
    #     position[square][PIECENAME] = ""

    def setEnpassantMove(self, enemy_pawn_square_index, new_square_index, old_square_index, position=None):

        if not isinstance(position, np.ndarray):
            position = self.position
        print("ENEMY EN PASSANT SQUARE: ", self.getSquareFromIndex(enemy_pawn_square_index))
        self.setMove(old_square_index, new_square_index)
        self.emptySquare(old_square_index, position)
        self.emptySquare(enemy_pawn_square_index, position)


    def castle(self, color, side, position=None):
        
        if not isinstance(position, np.ndarray):
            position = self.position

        if color == "WHITE":
          if side == "king_side":
              self.setMove(E1, G1, position)
              self.setMove(H1, F1, position)
          elif side == "queen_side":
              self.setMove(E1, C1, position)
              self.setMove(A1, D1, position)
        elif color == "BLACK":
            if side == "king_side":
                self.setMove(E8, G8, position)
                self.setMove(H8, F8, position)
            elif side == "queen_side":
                self.setMove(E8, C8, position)
                self.setMove(A8, D8, position)


    def setMove(self, old_square_index, new_square_index, position=None):

        if not isinstance(position, np.ndarray):
            position = self.position

        position[new_square_index] = position[old_square_index]
        self.emptySquare(old_square_index, position)


    def emptySquare(self, square_index, position=None):

        if not isinstance(position, np.ndarray):
            position = self.position

        position[square_index][COLOR] = ""
        position[square_index][PIECENAME] = ""


    def hasPiece(self, square_index, piece=None, position=None):
        if not isinstance(position, np.ndarray):
            position = self.position
        if piece:
            return position[square_index][PIECENAME] == piece
        else:
            return position[square_index][PIECENAME] != ""
        

    def hasColor(self, square_index, color, position=None):
        if not isinstance(position, np.ndarray):
            position = self.position
        return position[square_index][COLOR] == color
    
    @staticmethod
    def hasPieceOnSquare(square, piece_name = None):
        if piece_name:
            return square[PIECENAME] == piece_name
        return square[PIECENAME] != ""
    

    @staticmethod
    def hasColorOnSquare(square, color):
        return square[COLOR] == color


    def print(self, square):
        print(self.getRow(square))



    def printTable(self, position=None):
        if not isinstance(position, np.ndarray):
            position = self.position
        index = 0
        for values in position:
            print(f"{self.getSquareFromIndex(index)}: {values}")
            index += 1


    @staticmethod
    def copyTable(array):
        return np.copy(array)


if __name__ == "__main__":
    s = Position()
    # print(s.getRow('a1'))
    # print(timeit.timeit('s.copy(s.squareTable)', 'from __main__ import s', number=1000000))

    # print(s.getSquareFromPiece('KING', 'WHITE'))

    s.setMove(E1, E5)

    s.printTable()
