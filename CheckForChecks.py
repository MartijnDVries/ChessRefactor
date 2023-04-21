from config import*
from Singleton import Singleton
from SquareTable import SquareTable
import timeit
import ujson


class CheckForChecks(metaclass=Singleton):

  def __init__(self):
    self.tableClass = SquareTable()
    self.numbers = [row for row in range(1, 9)]
    self.files = 'abcdefgh'
    

  def is_in_check(self, own_color, table):
    king_square = self.tableClass.getSquareFromPiece('KING', own_color, table)
    king_square = king_square[0]

    for dir in ["left", "right"]:
      squares = self.horizontal_squares_from(king_square, dir)
      if self.check_horizontal_and_vertical_check(squares, table, own_color):
        return True
    for dir in ["up", "down"]:
      squares = self.vertical_squares_from(king_square, dir)
      if self.check_horizontal_and_vertical_check(squares, table, own_color):
        return True
    for dir in ["right_up", "right_down", "left_up", "left_down"]:
      squares = self.diagonal_squares_from(king_square, dir)
      if self.check_diagonal_check(squares, table, own_color):
        return True
    squares = self.knight_squares_from(king_square)
    if self.check_knight_check(squares, table, own_color):
      return True
    squares = self.pawn_squares_from(king_square, own_color)
    if self.check_pawn_check(squares, table, own_color):
      return True
    return False


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
        right_up_new_square = self.getNewSquare(right_up_new_square, 1, 1)
        squares.append(right_up_new_square)
      return filter_none(squares)
    if direction == "right_down":
      right_down_new_square = square
      while right_down_new_square is not None:
        right_down_new_square = self.getNewSquare(right_down_new_square, 1, -1)
        squares.append(right_down_new_square)
      return filter_none(squares)
    if direction == "left_up":
      left_up_new_square = square
      while left_up_new_square is not None:
        left_up_new_square = self.getNewSquare(left_up_new_square, -1, 1)
        squares.append(left_up_new_square)
      return filter_none(squares)
    if direction == "left_down":
      left_down_new_square = square
      while left_down_new_square is not None:
        left_down_new_square = self.getNewSquare(left_down_new_square, -1, -1)
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
    
  def pawn_squares_from(self, square, own_color):
    squares = []
    if own_color == "WHITE":
      squares.append(self.getNewSquare(square, 1, 1))
      squares.append(self.getNewSquare(square, -1, 1))
      return filter_none(squares)
    if own_color == "BLACK":
      squares.append(self.getNewSquare(square, 1, -1))
      squares.append(self.getNewSquare(square, -1, -1))
      return filter_none(squares)
    
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
  # s.setMove('h8', 'h5')
  # s.setMove('e1', 'e5')
  print(check.is_in_check("WHITE", s_list))

  # t = timeit.timeit('CheckForChecks().is_in_check("WHITE", s_list)', setup='from __main__ import CheckForChecks, s_list', number=100000)
  # print(t)


