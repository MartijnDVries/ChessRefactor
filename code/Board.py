import pygame
from config import *
from Singleton import Singleton


class ChessBoard(metaclass=Singleton):
  def __init__(self):
    self.rows = 8
    self.columns = 8
    self.start_X = BOARDLEFT
    self.start_Y = BOARDBOTTOM
    self.board = []
    self.COLOR = 0
    self.RECT = 1
    self.WHITE = WHITE
    self.BLACK = BLACK
    self.loadBoard()

  def loadBoard(self):
    self.board = []
    y = self.start_Y
    for row in range(self.rows):
      y -= SQUAREHEIGHT
      x = self.start_X
      if is_even(row):
        for col in range(self.columns):
          x += SQUAREWIDTH
          if is_even(col):
            self.board.append([self.WHITE, pygame.Rect(x, y, SQUAREWIDTH, SQUAREHEIGHT)])
            continue
          self.board.append([self.BLACK, pygame.Rect(x, y, SQUAREWIDTH, SQUAREHEIGHT)])
          continue
      else:
        for col in range(self.columns):
          x += SQUAREWIDTH
          if is_even(col):
            self.board.append([self.BLACK, pygame.Rect(x, y, SQUAREWIDTH, SQUAREHEIGHT)])
            continue
          self.board.append([self.WHITE, pygame.Rect(x, y, SQUAREWIDTH, SQUAREHEIGHT)])
          continue

  def draw(self, surface):
    if not self.board:
      self.loadBoard()
    for square in self.board:
      pygame.draw.rect(surface, square[self.COLOR], square[self.RECT])


  def setPosition(self, left, top):
    self.start_X = left
    self.start_Y = top - SQUAREHEIGHT
    self.loadBoard()

  def setSquareColor(self, white=WHITE, black=BLACK):
    self.WHITE = white
    self.BLACK = black
    self.loadBoard()
  

if __name__ == "__main__":
  c = ChessBoard()

