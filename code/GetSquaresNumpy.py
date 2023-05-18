from config import *
from SquareTableNumpy import SquareTableNumpy
from Singleton import Singleton
import numpy as np
import timeit


class GetSquaresNumpy(metaclass=Singleton):


    def __init__(self) -> None:
        self.tableClass = SquareTableNumpy()
        self.table = self.tableClass.squareTableNumpy
        self.numbers = [row for row in range(1, 9)]
        self.files = 'abcdefgh'
        self.topEdgeSquares = {56, 57, 58, 59, 60, 61, 62, 63}
        self.bottomRowEdgeSquares = {0, 1, 2, 3, 4, 5, 6, 7}
        self.leftEdgeSquares = {0, 8, 16, 24, 32, 40, 48, 56}
        self.rightEdgeSquares = {7, 15, 23, 31, 39, 47, 55, 63}
        self.secondRank = {8, 9, 10, 11, 12, 13, 14, 15}
        self.seventhRank = {48, 49, 50, 51, 52, 53, 54, 55}
        

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
        squares = set()
        if square not in self.leftEdgeSquares:
            squares.add(int(square - LEFT))
            if square not in self.topEdgeSquares:
                squares.add(int(square + LEFTUP))
            if square not in self.bottomRowEdgeSquares:
                squares.add(int(square - LEFTDOWN))
        if square not in self.rightEdgeSquares:
            squares.add(int(square + RIGHT))
            if square not in self.topEdgeSquares:
                squares.add(int(square + RIGHTUP))
            if square not in self.bottomRowEdgeSquares:
                squares.add(int(square - RIGHTDOWN))
        if square not in self.bottomRowEdgeSquares:
            squares.add(int(square - DOWN))
        if square not in self.topEdgeSquares:
            squares.add(int(square + UP))
        return squares
        

    def knight_squares_from(self, square):
        squares = []
        square = self.tableClass.getSquareFromIndex(square)
        squares.append(self.getNewSquare(square, 1, 2))
        squares.append(self.getNewSquare(square, 1, -2))
        squares.append(self.getNewSquare(square, -1, 2))
        squares.append(self.getNewSquare(square, -1, -2))
        squares.append(self.getNewSquare(square, 2, 1))
        squares.append(self.getNewSquare(square, 2, -1))
        squares.append(self.getNewSquare(square, -2, 1))
        squares.append(self.getNewSquare(square, -2, -1))

        squares =  filter_none(squares)
        
        squares = [self.tableClass.getSquareIndex(square) for square in squares]

        return squares


    def diagonal_squares_from(self, square, direction):
        if direction == "right_up":
            right_up_new_square = square
            while right_up_new_square not in self.topEdgeSquares\
                    and right_up_new_square not in self.rightEdgeSquares:
                right_up_new_square += RIGHTUP
                yield right_up_new_square
        if direction == "right_down":
            right_down_new_square = square
            while right_down_new_square not in self.bottomRowEdgeSquares\
                    and right_down_new_square not in self.rightEdgeSquares:
                right_down_new_square -= RIGHTDOWN
                yield right_down_new_square
        if direction == "left_up":
            left_up_new_square = square
            while left_up_new_square not in self.topEdgeSquares\
                    and left_up_new_square not in self.leftEdgeSquares:
                left_up_new_square += LEFTUP
                yield left_up_new_square
        if direction == "left_down":
            left_down_new_square = square
            while left_down_new_square not in self.bottomRowEdgeSquares\
                    and left_down_new_square not in self.leftEdgeSquares:
                left_down_new_square -= LEFTDOWN
                yield left_down_new_square


    def horizontal_squares_from(self, square, direction):
        if direction == "right":
            right_new_square = square
            while right_new_square not in self.rightEdgeSquares:
                right_new_square += RIGHT
                yield right_new_square
        if direction == "left":
            left_new_square = square
            while left_new_square not in self.leftEdgeSquares:
                left_new_square -= LEFT
                yield left_new_square


    def vertical_squares_from(self, square, directon):
        if directon == "up":
            up_new_square = square
            while up_new_square not in self.topEdgeSquares:
                up_new_square += UP
                yield up_new_square
        if directon == "down":
            down_new_square = square
            while down_new_square not in self.bottomRowEdgeSquares:
                down_new_square -= DOWN
                yield down_new_square


    def pawn_capture_squares_from(self, square, own_color):
        squares = set()
        if own_color == "WHITE":
            if square not in self.topEdgeSquares:
                if square not in self.leftEdgeSquares:
                    squares.add(int(square + LEFTUP))
                if square not in self.rightEdgeSquares:
                    squares.add(int(square +  RIGHTUP))
        if own_color == "BLACK":
            if square not in self.bottomRowEdgeSquares:
                if square not in self.leftEdgeSquares:
                    squares.add(int(square + LEFTDOWN))
                if square not in self.rightEdgeSquares:
                    squares.add(int(square + RIGHTDOWN))

        return squares

    def pawn_move_squares_from(self, square, own_color):
        squares = []
        if own_color == "WHITE":
            squares.append(int(square + UP))
            if square in self.secondRank:
                squares.append(int(square + 2 * UP))
            return squares
        if own_color == "BLACK":
            squares.append(int(square - DOWN))
            if square in self.seventhRank:
                squares.append(int(square - 2 * DOWN))
            return squares


if __name__ == "__main__":
    get = GetSquaresNumpy()
    s = SquareTableNumpy()
    # print(get.king_squares('e1'))
    # print(get.king_squares_numpy('e1'))


    def get_squares():
        return list(get.horizontal_squares_from_2(A1, "left"))

    print(get_squares())

    # print(timeit.timeit('get.horizontal_squares_from("e1", "right")', setup='from __main__ import get', number=1000000))

    # print(timeit.timeit('get_squares()', setup='from __main__ import get_squares', number=1000000))

    # print(timeit.timeit('get_squares_2()', setup='from __main__ import get_squares_2', number=1000000))