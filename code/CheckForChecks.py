from config import *
from Singleton import Singleton
from Position import Position
from GetSquares import GetSquares
import timeit
import ujson


class CheckForChecks(metaclass=Singleton):

    def __init__(self):
        self.positionHandler = Position()
        self.get = GetSquares()

    def is_in_check(self, own_color, position):
        king_square = self.positionHandler.getSquareFromPiece(
            'KING', own_color, position)

        for dir in ["left", "right"]:
            squares = list(self.get.horizontal_squares_from(king_square, dir))
            if self.check_horizontal_and_vertical_check(squares, position, own_color):
                return True

        for dir in ["up", "down"]:
            squares = list(self.get.vertical_squares_from(king_square, dir))
            if self.check_horizontal_and_vertical_check(squares, position, own_color):
                return True

        for dir in ["right_up", "right_down", "left_up", "left_down"]:
            squares = list(self.get.diagonal_squares_from(king_square, dir))
            if self.check_diagonal_check(squares, position, own_color):
                return True

        squares = self.get.knight_squares_from(king_square)
        if self.check_knight_check(squares, position, own_color):
            return True

        squares = self.get.pawn_capture_squares_from(king_square, own_color)
        if self.check_pawn_check(squares, position, own_color):
            return True
        return False

    def check_diagonal_check(self, squares, position, own_color):
        for square in squares:
            if self.positionHandler.hasColor(square, own_color, position):
                return False
            if self.positionHandler.hasPiece(square, 'BISHOP', position)\
                    or self.positionHandler.hasPiece(square, 'QUEEN', position):
                return True
        return False

    def check_pawn_check(self, squares, position, own_color):
        for square in squares:
            if not self.positionHandler.hasColor(square, own_color, position) \
                    and self.positionHandler.hasPiece(square, 'PAWN', position):
                return True
        return False

    def check_horizontal_and_vertical_check(self, squares, position, own_color):
        for square in squares:
            if self.positionHandler.hasColor(square, own_color, position):
                return False
            if self.positionHandler.hasPiece(square, 'ROOK', position)\
                    or self.positionHandler.hasPiece(square, 'QUEEN', position):
                return True
        return False

    def check_knight_check(self, squares, position, own_color):
        for square in squares:
            if self.positionHandler.hasPiece(square, 'KNIGHT', position)\
                    and not self.positionHandler.hasColor(square, own_color, position):
                return True


if __name__ == "__main__":
    check = CheckForChecks()
    s = Position()
    s_list = s.squareTableNumpy
    get = GetSquares()

    # squares = get.diagonal_squares_from('e1', 'right_up')

    # print(check.is_in_check_1("WHITE", s_list))
    # print(check.is_in_check_2("WHITE", s_list))
    # print(check.is_in_check_3("WHITE", s_list))
    print(check.is_in_check("BLACK", s_list))

    # print(timeit.timeit('check.is_in_check("WHITE", s_list)', setup='from __main__ import check, s_list, squares', number=100000))
