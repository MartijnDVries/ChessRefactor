from Singleton import Singleton
from config import *
import copy
import ujson
import json

class SquareTable(metaclass=Singleton):
  """Create a Table of the squares of the board which contain information about the status of the board at any given moment"""
  def __init__(self):
    self.squareTable = dict()
    self.setSquarePositions()
    self.setColor()
    self.setPieces()
    
  def __str__(self):
    return str(self.__dict__)
    

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

  def setColor(self):
    """Set default color on the squares"""
    for square in self.squareTable:
      row = int(square[1])
      if row == 1 or row == 2:
        self.squareTable[square].append("WHITE")
      elif row == 7 or row == 8:
        self.squareTable[square].append("BLACK")
      else:
        self.squareTable[square].append("")

  def setPieces(self):
    """Set up starting position"""
    for square in self.squareTable:
      row = int(square[1])
      file =  square[0]
      if row == 7 or row == 2:
        self.squareTable[square].append("PAWN")
        continue
      elif row == 1 or row  == 8:
        if file == 'a' or file =='h':
          self.squareTable[square].append("ROOK")
          continue
        elif file == 'b' or file == 'g':
          self.squareTable[square].append("KNIGHT")
        elif file == 'c' or file == 'f':
          self.squareTable[square].append("BISHOP")
        elif square == 'e1':
          self.squareTable[square].append("KING")
        elif square == 'e8':
          self.squareTable[square].append("KING")
        elif square == 'e8':
          self.squareTable[square].append("KING")
        elif square == 'd1':
          self.squareTable[square].append("QUEEN")
        elif square == 'd8':
          self.squareTable[square].append("QUEEN")
      else:
        self.squareTable[square].append("")

  def getTable(self):
    return self.squareTable

  def getRow(self, square):
    return f'\n\
    SQUARE: {square}\n\
    POSITIONS: {self.squareTable[square][POSITION]}\n\
    COLOR: {self.squareTable[square][COLOR]}\n\
    PIECE: {self.squareTable[square][PIECENAME]}\n'

  def getSquareFromPos(self, pos):
    pos_x = pos[0]
    pos_y = pos[1]
    square = list(filter(lambda s: self.squareTable[s][POSITION][0] in range(pos_x-37, pos_x+37) and self.squareTable[s][POSITION][1] in range(pos_y-37, pos_y+37), self.squareTable))
    return square[0]

  @staticmethod
  def getSquareFromPiece(piece_name, piece_color, table):
    square = list(filter(lambda s: table[s][PIECENAME] == piece_name.upper() and table[s][COLOR] == piece_color.upper(), table))
    return square
  
  @staticmethod
  def setStaticMove(old_square, new_square, table):
    table[new_square][COLOR] = table[old_square][COLOR]
    table[new_square][PIECENAME] = table[old_square][PIECENAME]
    SquareTable.emptyStaticSquare(old_square, table)
    return table

  @staticmethod
  def emptyStaticSquare(square, table):
    table[square][COLOR] = ""
    table[square][PIECENAME] = ""

  def setMove(self, old_square, new_square):
    self.squareTable[new_square][COLOR] = self.squareTable[old_square][COLOR]
    self.squareTable[new_square][PIECENAME] = self.squareTable[old_square][PIECENAME]
    self.emptySquare(old_square)

  def emptySquare(self, square):
    self.squareTable[square][COLOR] = ""
    self.squareTable[square][PIECENAME] = ""

  def print(self, square):
    print(self.getRow(square))

if __name__ == "__main__":
  s = SquareTable()
  # print(s.getFullTable())
  # s2 = copy.deepcopy(s.squareTable)
  # print(s2)
  # s.print('e1')
  # print(s.setStaticMove('e1', 'e5', s2)['e1'])
  # s.print('e1')
  table = ujson.loads(ujson.dumps(s.squareTable))

  s.setStaticMove('e1', 'e5', table)

  s.print('e5')

  print(table['e5'])
