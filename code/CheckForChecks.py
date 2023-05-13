from config import *
from Singleton import Singleton
from SquareTable import SquareTable
from SquareTableNumpy import SquareTableNumpy
from GetSquares import GetSquares
import timeit
import ujson


class CheckForChecks(metaclass=Singleton):

    def __init__(self):
        self.tableClass = SquareTableNumpy()
        self.get = GetSquares()

    def is_in_check(self, own_color, table):
        king_square = self.tableClass.getSquareFromPiece(
            'KING', own_color, table)
        # king_square = king_square[0]

        for dir in ["left", "right"]:
            squares = self.get.horizontal_squares_from(king_square, dir)
            if self.check_horizontal_and_vertical_check(squares, table, own_color):
                return True
        for dir in ["up", "down"]:
            squares = self.get.vertical_squares_from(king_square, dir)
            if self.check_horizontal_and_vertical_check(squares, table, own_color):
                return True
        for dir in ["right_up", "right_down", "left_up", "left_down"]:
            squares = self.get.diagonal_squares_from(king_square, dir)
            if self.check_diagonal_check(squares, table, own_color):
                return True
        squares = self.get.knight_squares_from(king_square)
        if self.check_knight_check(squares, table, own_color):
            return True
        squares = self.get.pawn_capture_squares_from(king_square, own_color)
        if self.check_pawn_check(squares, table, own_color):
            return True
        return False

    def check_diagonal_check(self, squares, table, own_color):
        for square in squares:
            if not self.tableClass.hasPiece(square, table=table):
                continue
            if self.tableClass.hasColor(square, own_color, table):
                return False
            if self.tableClass.hasPiece(square, 'BISHOP', table)\
                    or self.tableClass.hasPiece(square, 'QUEEN', table):
                return True
        return False


    def check_pawn_check(self, squares, table, own_color):
        for square in squares:
            if not self.tableClass.hasColor(square, own_color, table) \
                    and self.tableClass.hasPiece(square, 'PAWN', table):
                return True
        return False

    def check_horizontal_and_vertical_check(self, squares, table, own_color):
        for square in squares:
            if not self.tableClass.hasPiece(square, table=table):
                continue
            if self.tableClass.hasColor(square, own_color, table):
                return False
            if self.tableClass.hasPiece(square, 'ROOK', table)\
                    or self.tableClass.hasPiece(square, 'QUEEN', table):
                return True
        return False

    def check_knight_check(self, squares, table, own_color):
        for square in squares:
            if self.tableClass.hasPiece(square, 'KNIGHT', table)\
                  and not self.tableClass.hasColor(square, own_color, table):
                return True


if __name__ == "__main__":
    check = CheckForChecks()
    s = SquareTableNumpy()
    s_list = s.squareTableNumpy
    # s.setMove('h8', 'h5')
    # s.setMove('e1', 'e5')
    # print(check.is_in_check("WHITE", s_list))

    t = timeit.timeit('check.is_in_check("WHITE", s_list)', setup='from __main__ import check, s_list', number=100000)
    print(t)
