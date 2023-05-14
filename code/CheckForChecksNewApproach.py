from config import *
from Singleton import Singleton
from SquareTableNewApproach import SquareTableNewApproach
from GetSquaresNewApproach import GetSquaresNewApproach
import timeit
import ujson


class CheckForChecksNewApproach(metaclass=Singleton):

    def __init__(self):
        self.tableClass = SquareTableNewApproach()
        self.get = GetSquaresNewApproach()

    def is_in_check(self, own_color, position):
        king_square = self.tableClass.getSquareFromPiece(
            'KING', own_color, position)


        for dir in ["left", "right"]:
            squares = list(self.get.horizontal_squares_from(king_square, dir, position))
            if self.check_horizontal_and_vertical_check(squares, own_color):
                return True
            
        for dir in ["up", "down"]:
            squares = list(self.get.vertical_squares_from(king_square, dir, position))
            if self.check_horizontal_and_vertical_check(squares, own_color):
                return True
            
        for dir in ["right_up", "right_down", "left_up", "left_down"]:
            squares = list(self.get.diagonal_squares_from(king_square, dir, position))
            if self.check_diagonal_check(squares, own_color):
                return True
            
        squares = self.get.knight_squares_from(king_square, position)
        if self.check_knight_check(squares, own_color):
            return True
        
        squares = list(self.get.pawn_capture_squares_from(king_square, own_color, position))
        if self.check_pawn_check(squares, own_color):
            return True

        return False
    

    def check_diagonal_check(self, squares, own_color):
        for square in squares:
            if self.tableClass.hasColor(square, own_color):
                return False
            if self.tableClass.hasPiece(square, 'BISHOP')\
                    or self.tableClass.hasPiece(square, 'QUEEN'):
                return True
        return False
    

    def check_pawn_check(self, squares, own_color):
        for square in squares:
            if not self.tableClass.hasColor(square, own_color) \
                    and self.tableClass.hasPiece(square, 'PAWN'):
                return True
        return False


    def check_horizontal_and_vertical_check(self, squares, own_color):
        for square in squares:
            if self.tableClass.hasColor(square, own_color):
                return False
            if self.tableClass.hasPiece(square, 'ROOK')\
                    or self.tableClass.hasPiece(square, 'QUEEN'):
                return True
        return False


    def check_knight_check(self, squares, own_color):
        for square in squares:
            if self.tableClass.hasPiece(square, 'KNIGHT')\
                  and not self.tableClass.hasColor(square, own_color):
                return True


if __name__ == "__main__":
    check = CheckForChecksNewApproach()
    s = SquareTableNewApproach()
    s_list = s.squareTableNumpy
    get = GetSquaresNewApproach()

    print(check.is_in_check("WHITE", s_list))

    # print(timeit.timeit('check.is_in_check("WHITE", s_list)', setup='from __main__ import check, s_list, squares', number=100000))
