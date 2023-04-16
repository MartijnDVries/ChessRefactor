from Board import ChessBoard
from SquareTable import SquareTable
from ChessPiece import Piece
from Singleton import Singleton
from config import *



class ServiceContainer(metaclass=Singleton):

  def __init__(self):
    self.board = ChessBoard()
    self.squareTableClass = SquareTable()
    self.squareTable = self.squareTableClass.squareTable
    self.board.setSquareColor(WHITE, (120, 17, 17))
    self.pieceCollection = self.getCollection()

  def parseTable(self, piece, color):
      piece = piece.lower()
      color = color.lower()
      image_file = f"{color}_{piece}"
      return image_file, color

  def getCollection(self):
    table = self.squareTable
    pieceCollection = []
    POSITION = 0
    OCCUPIED = 1
    COLOR = 2
    PIECENAME = 3
    for square in table:
      if table[square][OCCUPIED]:
        pieceCollection.append(Piece(*self.parseTable(table[square][PIECENAME], table[square][COLOR]), square, table[square][POSITION], table[square][PIECENAME]))
    return pieceCollection

