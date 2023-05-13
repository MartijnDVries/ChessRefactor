from config import *
from SquareTable import SquareTable
from Singleton import Singleton
import timeit

class GetSquares(metaclass=Singleton):


    def __init__(self) -> None:
        self.tableClass = SquareTable()
        self.table = self.tableClass.getTable()
        self.numbers = [row for row in range(1, 9)]
        self.files = 'abcdefgh'


    def getNewSquare(self, square, add_file, add_square_number):
        file_index = self.files.index(str(square[0]))
        square_number_index = self.numbers.index(int(square[1]))

        new_file_index = file_index + add_file
        new_square_number_index = square_number_index + add_square_number

        if new_file_index < 0\
                or new_file_index > 7\
                or new_square_number_index < 0\
                or new_square_number_index > 7:
            return None

        return f"{self.files[new_file_index]}{self.numbers[new_square_number_index]}"


    def king_squares(self, square):
        squares = []
        squares.append(self.getNewSquare(square, 1, 1))
        squares.append(self.getNewSquare(square, 1, -1))
        squares.append(self.getNewSquare(square, 1, 0))
        squares.append(self.getNewSquare(square, -1, 1))
        squares.append(self.getNewSquare(square, -1, -1))
        squares.append(self.getNewSquare(square, -1, 0))
        squares.append(self.getNewSquare(square, 0, 1))
        squares.append(self.getNewSquare(square, 0, -1))
        return filter_none(squares)


    def knight_squares_from(self, square):
        squares = []
        squares.append(self.getNewSquare(square, 1, 2))
        squares.append(self.getNewSquare(square, 1, -2))
        squares.append(self.getNewSquare(square, -1, 2))
        squares.append(self.getNewSquare(square, -1, -2))
        squares.append(self.getNewSquare(square, 2, 1))
        squares.append(self.getNewSquare(square, 2, -1))
        squares.append(self.getNewSquare(square, -2, 1))
        squares.append(self.getNewSquare(square, -2, -1))
        return filter_none(squares)


    def diagonal_squares_from(self, square, direction):
        squares = []
        if direction == "right_up":
            right_up_new_square = square
            while right_up_new_square is not None:
                right_up_new_square = self.getNewSquare(
                    right_up_new_square, 1, 1)
                squares.append(right_up_new_square)
            return filter_none(squares)
        if direction == "right_down":
            right_down_new_square = square
            while right_down_new_square is not None:
                right_down_new_square = self.getNewSquare(
                    right_down_new_square, 1, -1)
                squares.append(right_down_new_square)
            return filter_none(squares)
        if direction == "left_up":
            left_up_new_square = square
            while left_up_new_square is not None:
                left_up_new_square = self.getNewSquare(
                    left_up_new_square, -1, 1)
                squares.append(left_up_new_square)
            return filter_none(squares)
        if direction == "left_down":
            left_down_new_square = square
            while left_down_new_square is not None:
                left_down_new_square = self.getNewSquare(
                    left_down_new_square, -1, -1)
                squares.append(left_down_new_square)
            return filter_none(squares)


    def horizontal_squares_from(self, square, direction):
        squares = []
        if direction == "right":
            right_new_square = square
            while right_new_square is not None:
                right_new_square = self.getNewSquare(right_new_square, 1, 0)
                squares.append(right_new_square)
            return filter_none(squares)
        if direction == "left":
            left_new_square = square
            while left_new_square is not None:
                left_new_square = self.getNewSquare(left_new_square, -1, 0)
                squares.append(left_new_square)
            return filter_none(squares)


    def vertical_squares_from(self, square, directon):
        squares = []
        if directon == "up":
            up_new_square = square
            while up_new_square is not None:
                up_new_square = self.getNewSquare(up_new_square, 0, 1)
                squares.append(up_new_square)
            return filter_none(squares)
        if directon == "down":
            down_new_square = square
            while down_new_square is not None:
                down_new_square = self.getNewSquare(down_new_square, 0, -1)
                squares.append(down_new_square)
            return filter_none(squares)


    def pawn_capture_squares_from(self, square, own_color):
        squares = []
        if own_color == "WHITE":
            squares.append(self.getNewSquare(square, 1, 1))
            squares.append(self.getNewSquare(square, -1, 1))
            return filter_none(squares)
        if own_color == "BLACK":
            squares.append(self.getNewSquare(square, 1, -1))
            squares.append(self.getNewSquare(square, -1, -1))
            return filter_none(squares)


    def pawn_move_squares_from(self, square, own_color):
        squares = []
        pawn_row = int(square[1])
        if own_color == "WHITE":
            squares.append(self.getNewSquare(square, 0, 1))
            if pawn_row == 2:
                squares.append(self.getNewSquare(square, 0, 2))
            return filter_none(squares)
        if own_color == "BLACK":
            squares.append(self.getNewSquare(square, 0, -1))
            if pawn_row == 7:
                squares.append(self.getNewSquare(square, 0, -2))
            return filter_none(squares)


if __name__ == "__main__":
    get = GetSquares()
    print(get.diagonal_squares_from('e5', 'right_up'))
    print(get.pawn_move_squares_from('e2'))
