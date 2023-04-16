from Singleton import Singleton
from config import *


class SquareTable(metaclass=Singleton):
  """Create a Table of the squares of the board which contain information about the status of the board at any given moment"""
  def __init__(self):
    self.squareTable = dict()
    self.setSquarePositions()
    self.setOccupied()
    self.setPieces()
    

  def setSquarePositions(self):
    """Center X, Y for all squares attached to squarename"""

    chars = "abcdefgh"

    self.squareTable = dict()

    start_x = 100 + 37
    start_y = 646 + 37

    for row in range(1, 9):
      x = start_x
      start_y -= 74
      for col in chars:
        x += 74
        square = col + str(row)
        self.squareTable[square] = [[x, start_y]]

  def setOccupied(self):
    """Set default occupied"""
    for square in self.squareTable:
      row = int(square[1])
      if row == 1 or row == 2:
        self.squareTable[square].extend([True, "WHITE"])
      elif row == 7 or row == 8:
        self.squareTable[square].extend([True, "BLACK"])
      else:
        self.squareTable[square].extend([False, ""])

  def setPieces(self):
    """Set up starting position"""
    for square in self.squareTable:
      if square == 'a1':
        self.squareTable[square].append("ROOK")
      elif square == 'a2':
        self.squareTable[square].append("PAWN")
      elif square == 'a7':
        self.squareTable[square].append("PAWN")
      elif square == 'a8':
        self.squareTable[square].append("ROOK")
      elif square == 'b1':
        self.squareTable[square].append("KNIGHT")
      elif square == 'b2':
        self.squareTable[square].append("PAWN")
      elif square == 'b7':
        self.squareTable[square].append("PAWN")
      elif square == 'b8':
        self.squareTable[square].append("KNIGHT")
      elif square == 'c1':
        self.squareTable[square].append("BISHOP")
      elif square == 'c2':
        self.squareTable[square].append("PAWN")
      elif square == 'c7':
        self.squareTable[square].append("PAWN")
      elif square == 'c8':
        self.squareTable[square].append("BISHOP")
      elif square == 'd1':
        self.squareTable[square].append("QUEEN")
      elif square == 'd2':
        self.squareTable[square].append("PAWN")
      elif square == 'd7':
        self.squareTable[square].append("PAWN")
      elif square == 'd8':
        self.squareTable[square].append("KING")
      elif square == 'e1':
        self.squareTable[square].append("KING")
      elif square == 'e2':
        self.squareTable[square].append("PAWN")
      elif square == 'e7':
        self.squareTable[square].append("PAWN")
      elif square == 'e8':
        self.squareTable[square].append("QUEEN")
      elif square == 'f1':
        self.squareTable[square].append("BISHOP")
      elif square == 'f2':
        self.squareTable[square].append("PAWN")
      elif square == 'f7':
        self.squareTable[square].append("PAWN")
      elif square == 'f8':
        self.squareTable[square].append("BISHOP")
      elif square == 'g1':
        self.squareTable[square].append("KNIGHT")
      elif square == 'g2':
        self.squareTable[square].append("PAWN")
      elif square == 'g7':
        self.squareTable[square].append("PAWN")
      elif square == 'g8':
        self.squareTable[square].append("KNIGHT")
      elif square == 'h1':
        self.squareTable[square].append("ROOK")
      elif square == 'h2':
        self.squareTable[square].append("PAWN")
      elif square == 'h7':
        self.squareTable[square].append("PAWN")
      elif square == 'h8':
        self.squareTable[square].append("ROOK")
      else:
        self.squareTable[square].append("")

  def getFullTable(self):
    return self.squareTable

  def getPositions(self, square):
    return self.squareTable[square][POSITION]

  def getOccupied(self, square):
    return self.squareTable[square][OCCUPIED]

  def getRow(self, square):
    return f'\n\
    SQUARE: {square}\n\
    POSITIONS: {self.squareTable[square][POSITION]}\n\
    OCCUPIED: {str(self.squareTable[square][OCCUPIED])}\n\
    COLOR: {self.squareTable[square][COLOR]}\n\
    PIECE: {self.squareTable[square][PIECENAME]}'

  def getSquareFromPos(self, pos):
    pos_x = pos[0]
    pos_y = pos[1]
    square = list(filter(lambda s: self.squareTable[s][POSITION][0] in range(pos_x-37, pos_x+37) and self.squareTable[s][POSITION][1] in range(pos_y-37, pos_y+37), self.squareTable))
    return square[0]

  def getSquareFromPiece(self, piece_name, piece_color):
    square = list(filter(lambda s: self.squareTable[s][PIECENAME] == piece_name.upper() and self.squareTable[s][COLOR] == piece_color.upper(), self.squareTable))
    return square

  def setMove(self, old_square, new_square):
    self.squareTable[new_square][OCCUPIED] = self.squareTable[old_square][OCCUPIED]
    self.squareTable[new_square][COLOR] = self.squareTable[old_square][COLOR]
    self.squareTable[new_square][PIECENAME] = self.squareTable[old_square][PIECENAME]
    self.emptySquare(old_square)

  def emptySquare(self, square):
    self.squareTable[square][OCCUPIED] = False
    self.squareTable[square][COLOR] = ""
    self.squareTable[square][PIECENAME] = ""

  def print(self, square):
    print(self.getRow(square))

if __name__ == "__main__":
  s = SquareTable()
  # print(s.getFullTable())
  print(s.getRow('h1'))
  s.emptySquare('h1')
  print(s.getRow('h1'))
  s.setMove('b1', 'h1')
  s.print('b1')
  s.print('h1')


