from config import*
from Singleton import Singleton
from SquareTable import SquareTable


class LegalMoves(metaclass=Singleton):

  def __init__(self):
    self.tableClass = SquareTable()
    self.table = self.tableClass.squareTable
    self.numbers = [row for row in range(1, 9)]
    self.files = 'abcdefgh'

  def is_legal(self, old_square, new_square):
    return True
 
  def is_in_check(self, king_color):
    king_square = self.tableClass.getSquareFromPiece('KING', king_color)
    print(king_square[0])
  
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
    yield self.getNewSquare(square, 1, 2)
    yield self.getNewSquare(square, 1, -2)
    yield self.getNewSquare(square, -1, 2)
    yield self.getNewSquare(square, -1, -2)
    yield self.getNewSquare(square, 2, 1)
    yield self.getNewSquare(square, 2, -1)
    yield self.getNewSquare(square, -2, 1)
    yield self.getNewSquare(square, -2, -1)


  def bishop_squares_from(self, square):
    right_up_new_square = square
    right_down_new_square = square
    left_up_new_square = square
    while new_square is not None:
      new_square = self.getNewSquare(new_square, 1, 1)
      yield new_square
    while new_square is not None:
      new_square = self.getNewSquare(new_square, 1, 1)
      yield new_square


  

if __name__ == "__main__":
  l = LegalMoves()
  # l.is_in_check('white')
  fa = l.bishop_squares_from('e5')
  print(fa)