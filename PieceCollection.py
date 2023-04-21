from config import *
from ChessPiece import Piece
from Singleton import Singleton
from SquareTable import SquareTable


class PieceCollection(metaclass=Singleton):
  def __init__(self):
    self.tableClass = SquareTable()
    self.table = self.tableClass.squareTable
    self.pieceCollection = self.getCollection()

  def parseTable(self, piece, color):
      piece = piece.lower()
      color = color.lower()
      image_file = f"{color}_{piece}"
      return image_file, color

  def getCollection(self):
    pieceCollection = []
    for square in self.table:
      if self.table[square][PIECENAME]:
        pieceCollection.append(Piece(*self.parseTable(self.table[square][PIECENAME], self.table[square][COLOR]), square, self.table[square][POSITION], self.table[square][PIECENAME]))
    return pieceCollection

 

if __name__ == "__main__":
  p = PieceCollection()