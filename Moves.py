from config import*
from Singleton import Singleton
from SquareTable import SquareTable
import copy


class LegalMoves(metaclass=Singleton):


  def __init__(self):
    self.tableClass = SquareTable()
    self.table = self.tableClass.squareTable
    self.numbers = [row for row in range(1, 9)]
    self.files = 'abcdefgh'

  def is_legal(self, old_square, new_square):
    return True
 
  def is_in_check(self, own_color, table):
    king_square = self.tableClass.getSquareFromPiece('KING', own_color, table)
    king_square = king_square[0]
    squares = self.diagonal_squares_from(king_square, "right_up")
    if self.check_diagonal_check(squares, table, own_color):
      return True
    
    squares = self.horizontal_squares_from('e5', 'right')
    if self.check_horizontal_and_vertical_check(squares, table, own_color):
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
      while left_up_new_square is not None:
        left_up_new_square = self.getNewSquare(left_up_new_square, -1, 1)
        squares.append(left_up_new_square)
      return filter_none(squares)
    if direction == "left_down":
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
        square.append(left_new_square)
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

  def check_diagonal_check(self, squares, table, own_color):
    for square in squares:
      if not table[square][PIECENAME]:
        continue
      if table[square][COLOR] == own_color:
        return False
      if table[square][PIECENAME] == "BISHOP" or table[square][PIECENAME] == "QUEEN":
        return True
    return False

    
  def check_pawn_check(self, square, table, own_color):
    if own_color == "WHITE":
      pawn_square_1 = self.getNewSquare(square, 1, 1)
      if table[pawn_square_1][COLOR] != own_color and table[pawn_square_1][PIECENAME] == "PAWN":
        return True
      pawn_square_2 = self.getNewSquare(square, -1, 1)
      if table[pawn_square_2][COLOR] != own_color and table[pawn_square_2][PIECENAME] == "PAWN":
        return True
      return False
    if own_color == "BLACK":
      pawn_square_1 = self.getNewSquare(square, 1, -1)
      if table[pawn_square_1][COLOR] != own_color and table[pawn_square_1][PIECENAME] == "PAWN":
        return True
      pawn_square_2 = self.getNewSquare(square, -1, -1)
      if table[pawn_square_2][COLOR] != own_color and table[pawn_square_2][PIECENAME] == "PAWN":
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

  

if __name__ == "__main__":
  l = LegalMoves()
  s = SquareTable()
  s_list = s.squareTable

  s.setMove('e1', 'e5')
  s.setMove('h8', 'h5')
  print(s_list['e5'])
  print(s_list['h5'])
  print(l.is_in_check("WHITE", s_list))
  # print(l.is_in_check('WHITE', s_list))
  # s2 = copy.deepcopy(s_list)
  # l.is_in_check('WHITE', s2)
  # print(l.diagonal_squares_from('e1', 'right_up'))
  # print(l.diagonal_squares_from('e1', 'right_up'))
