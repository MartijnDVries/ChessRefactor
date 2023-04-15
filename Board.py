import pygame
from config import *



class ChessBoard:
  def __init__(self):
    self.rows = 8
    self.columns = 8
    self.start_X = 100
    self.start_Y = -20
    self.board = []
    self.COLOR = 0
    self.RECT = 1
    self.WHITE = WHITE
    self.BLACK = BLACK
    self.initBoard()

  def initBoard(self):
    y = self.start_Y
    for row in range(self.rows):
      y += SQUAREHEIGHT
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
      self.initBoard()
    for square in self.board:
      pygame.draw.rect(surface, square[self.COLOR], square[self.RECT])


  def events(self):
    pos = pygame.mouse.get_pos()
    for square in self.board:
      if square[self.RECT].collidepoint(pos):
        print(square[self.COLOR])

  def setPosition(self, left, top):
    self.start_X = left
    self.start_Y = top - 74
    self.initBoard()
  

if __name__ == "__main__":
  c = ChessBoard()
  c.draw()
