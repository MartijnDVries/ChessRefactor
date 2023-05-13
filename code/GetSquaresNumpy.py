from config import *
from SquareTableNumpy import SquareTableNumpy
from Singleton import Singleton
import numpy as np
import timeit


class GetSquares(metaclass=Singleton):


    def __init__(self) -> None:
        self.tableClass = SquareTableNumpy()
        self.table = self.tableClass.squareTableNumpy
        self.numbers = [row for row in range(1, 9)]
        self.files = 'abcdefgh'
        self.topEdgeSquares = {56, 57, 58, 58, 60, 61, 62, 63}
        self.bottomRowEdgeSquares = {0, 1, 2, 3, 4, 5, 6, 7}
        self.leftEdgeSquares = {0, 8, 16, 24, 32, 40, 48, 46}
        self.rightEdgeSquares = {7, 15, 23, 31, 39, 47, 55, 63}
        

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
    

    def king_squares_numpy(self, square):
        squares = set()
        index =  self.tableClass.getSquareIndex(square)
        if index not in self.leftEdgeSquares:
            squares.add(int(index - 1))
            if index not in self.topEdgeSquares:
                squares.add(int(index + 7))
            if index not in self.bottomRowEdgeSquares:
                squares.add(int(index - 9))
        if index not in self.rightEdgeSquares:
            squares.add(int(index + 1))
            if index not in self.topEdgeSquares:
                squares.add(int(index + 9))
            if index not in self.bottomRowEdgeSquares:
                squares.add(int(index - 7))
        if index not in self.bottomRowEdgeSquares:
            squares.add(int(index - 8))
        if index not in self.topEdgeSquares:
            squares.add(int(index + 8))
        return squares
        





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

    print(get.king_squares('e1'))
    print(get.king_squares_numpy('e1'))

    # timeit.timeit('GetSquares().king_squares("e1")', setup='from __ main__ import GetSquares', number=10000)
    # timeit.timeit('GetSquares().king_squares_numpy("e1")', setup='from __ main__ import GetSquares', number=10000)


    print(timeit.timeit('get.king_squares("e1")', setup='from __main__ import get', number=100000))

    print(timeit.timeit('get.king_squares_numpy("e1")', setup='from __main__ import get', number=100000))