from config import *
from SquareTableNewApproach import SquareTableNewApproach
from Singleton import Singleton
import numpy as np
import timeit


class GetSquaresNewApproach(metaclass=Singleton):


    def __init__(self) -> None:
        self.tableClass = SquareTableNewApproach()
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
        squares = set()
        index =  self.tableClass.getSquareIndex(square)
        if index not in self.leftEdgeSquares:
            squares.add(int(index - LEFT))
            if index not in self.topEdgeSquares:
                squares.add(int(index + LEFTUP))
            if index not in self.bottomRowEdgeSquares:
                squares.add(int(index - LEFTDOWN))
        if index not in self.rightEdgeSquares:
            squares.add(int(index + RIGHT))
            if index not in self.topEdgeSquares:
                squares.add(int(index + RIGHTUP))
            if index not in self.bottomRowEdgeSquares:
                squares.add(int(index - RIGHTDOWN))
        if index not in self.bottomRowEdgeSquares:
            squares.add(int(index - DOWN))
        if index not in self.topEdgeSquares:
            squares.add(int(index + UP))
        return squares
        

    def knight_squares_from(self, square, position):
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
        
        squares = [position[self.tableClass.getSquareIndex(square)] for square in squares]

        return squares


    def diagonal_squares_from(self, square, direction, position):
        if direction == "right_up":
            right_up_new_square = square
            while right_up_new_square not in self.topEdgeSquares\
                    and right_up_new_square not in self.rightEdgeSquares:
                right_up_new_square += RIGHTUP
                yield position[right_up_new_square]
        if direction == "right_down":
            right_down_new_square = square
            while right_down_new_square not in self.bottomRowEdgeSquares\
                    and right_down_new_square not in self.rightEdgeSquares:
                right_down_new_square -= RIGHTDOWN
                yield position[right_down_new_square]
        if direction == "left_up":
            left_up_new_square = square
            while left_up_new_square not in self.topEdgeSquares\
                    and left_up_new_square not in self.leftEdgeSquares:
                left_up_new_square += LEFTUP
                yield position[left_up_new_square]
        if direction == "left_down":
            left_down_new_square = square
            while left_down_new_square not in self.bottomRowEdgeSquares\
                    and left_down_new_square not in self.leftEdgeSquares:
                left_down_new_square -= LEFTDOWN
                yield position[left_down_new_square]


    def horizontal_squares_from(self, square, direction, position):
        if direction == "right":
            right_new_square = square
            while right_new_square not in self.rightEdgeSquares:
                right_new_square += RIGHT
                yield position[right_new_square]
        if direction == "left":
            left_new_square = square
            while left_new_square not in self.leftEdgeSquares:
                left_new_square -= LEFT
                yield position[left_new_square]



    def vertical_squares_from(self, square, directon, position):
        if directon == "up":
            up_new_square = square
            while up_new_square not in self.topEdgeSquares:
                up_new_square += UP
                yield position[up_new_square]
        if directon == "down":
            down_new_square = square
            while down_new_square not in self.bottomRowEdgeSquares:
                down_new_square -= DOWN
                yield position[down_new_square]


    def pawn_capture_squares_from(self, square, own_color, position):
        while True:
          if own_color == "WHITE":
              if square not in self.topEdgeSquares:
                  if square not in self.leftEdgeSquares:
                      yield position[square + LEFTUP]
                  if square not in self.rightEdgeSquares:
                      yield position[square + RIGHTUP]
              break
          if own_color == "BLACK":
              if square not in self.bottomRowEdgeSquares:
                  if square not in self.leftEdgeSquares:
                      yield position[square - LEFTDOWN]
                  if square not in self.rightEdgeSquares:
                      yield position[square - RIGHTDOWN]
              break

 
    def pawn_move_squares_from(self, square, own_color):
        squares = []
        pawn_row = int(square[1])
        if own_color == "WHITE":
            squares.append(int(square + UP))
            if pawn_row == 2:
                squares.append(int(square + 2 * UP))
            return squares
        if own_color == "BLACK":
            squares.append(int(square - DOWN))
            if pawn_row == 7:
                squares.append(int(square - 2 * DOWN))
            return squares


if __name__ == "__main__":
    get = GetSquaresNewApproach()
    s = SquareTableNewApproach()
    # print(get.king_squares('e1'))
    # print(get.king_squares_numpy('e1'))


    def get_squares():
        return list(get.horizontal_squares_from(E1, "left", position=s.squareTableNumpy))

    print(get_squares())
    # def get_squares_2():
    #     for index in get.horizontal_squares_from_2("e1", "left"):
    #         square = s.getSquareFromIndex(index)
    #         print(square)


    # print(get_squares())
    # get_squares_2()

    # print(list(get.horizontal_squares_from_2("e1", "left")))
    # timeit.timeit('GetSquares().king_squares("e1")', setup='from __ main__ import GetSquares', number=10000)
    # timeit.timeit('GetSquares().king_squares_numpy("e1")', setup='from __ main__ import GetSquares', number=10000)


    # print(timeit.timeit('get.horizontal_squares_from("e1", "right")', setup='from __main__ import get', number=1000000))

    # print(timeit.timeit('get_squares()', setup='from __main__ import get_squares', number=1000000))

    # print(timeit.timeit('get_squares_2()', setup='from __main__ import get_squares_2', number=1000000))