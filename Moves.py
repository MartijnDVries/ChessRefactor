from config import*
from Singleton import Singleton
from SquareTable import SquareTable


class LegalMoves(metaclass=Singleton):

  def __init__(self):
    self.tableClass = SquareTable()
    self.table = self.tableClass.squareTable

  def is_legal(self, old_square, new_square):
    return True
 
  def is_in_check(self, king_color):
    king_square = self.tableClass.getSquareFromPiece('KING', king_color)
    print(king_square[0])



if __name__ == "__main__":
  l = LegalMoves()
  l.is_in_check('white')