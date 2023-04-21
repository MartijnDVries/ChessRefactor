import pygame
from config import *
from PieceCollection import PieceCollection
from Moves import LegalMoves
from SquareTable import SquareTable

class EventChecker:

  def __init__(self):
    self.eventCollection = {'game': self.game, 'main_menu': self.main_menu}
    self.piecesInstance = PieceCollection()
    self.pieces = self.piecesInstance.pieceCollection
    self.tableClass = SquareTable()
    self.table = self.tableClass.squareTable
    self.move = LegalMoves()

  def loadEvents(self, view, event):
    return self.eventCollection[view](event)

  def mouseDownEventGame(self, event):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      for piece in self.pieces:
        piece.setActive(pos)
    
  def mouseMoveEventGame(self, event):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      for piece in self.pieces:
        piece.dragTo(pos)

  def mouseUpEventGame(self, event):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
      for piece in self.pieces:
        if piece.active:  
            self.checkMove(piece, pos)
            piece.place()

  def checkMove(self, piece, pos):
    if is_inside_board(pos):
      new_square = self.tableClass.getSquareFromPos(pos)
      if self.move.is_legal(piece.square, new_square, piece.name):
        self.tableClass.setMove(piece.square, new_square)
        new_pos = self.table[new_square][POSITION]
        piece.update(new_pos, new_square)
        return
    piece.placeback()


  def game(self, event):
    self.mouseDownEventGame(event)
    self.mouseUpEventGame(event)
    self.mouseMoveEventGame(event)

  def main_menu(self):
    pass
