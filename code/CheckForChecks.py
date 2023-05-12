from config import *
from Singleton import Singleton
from SquareTable import SquareTable
from GetSquares import GetSquares
import timeit
import ujson


class CheckForChecks(metaclass=Singleton):

    def __init__(self):
        self.tableClass = SquareTable()
        self.get = GetSquares()

    def is_in_check(self, own_color, table):
        king_square = self.tableClass.getSquareFromPiece(
            'KING', own_color, table)
        king_square = king_square[0]

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
            if not table[square][PIECENAME]:
                continue
            if table[square][COLOR] == own_color:
                return False
            if table[square][PIECENAME] == "BISHOP" or table[square][PIECENAME] == "QUEEN":
                return True
        return False

    def check_pawn_check(self, squares, table, own_color):
        for square in squares:
            if table[square][COLOR] != own_color and table[square][PIECENAME] == "PAWN":
                return True
        return False

    def check_horizontal_and_vertical_check(self, squares, table, own_color):
        for square in squares:
            if not table[square][PIECENAME]:
                continue
            if table[square][COLOR] == own_color:
                return False
            if table[square][PIECENAME] == "ROOK" or table[square][PIECENAME] == "QUEEN":
                return True
        return False

    def check_knight_check(self, squares, table, own_color):
        for square in squares:
            if table[square][PIECENAME] == "KNIGHT" and table[square][COLOR] != own_color:
                return True


if __name__ == "__main__":
    check = CheckForChecks()
    s = SquareTable()
    s_list = s.squareTable
    print(s.squareTable)
    # s.setMove('h8', 'h5')
    # s.setMove('e1', 'e5')
    print(check.is_in_check("WHITE", s_list))

    # t = timeit.timeit('CheckForChecks().is_in_check("WHITE", s_list)', setup='from __main__ import CheckForChecks, s_list', number=100000)
    # print(t)
