import pygame
from Container import ServiceContainer
from config import *


class EventChecker:

  def __init__(self):
    self.container = ServiceContainer()
    self.eventCollection = {'game': self.game, 'main_menu': self.main_menu}
    self.board = self.container.board
    self.pieces = self.container.pieceCollection
    self.table = self.container.squareTableClass
    self.pos = pygame.mouse.get_pos()

  def loadEvents(self, view, event):
    return self.eventCollection[view](event)

  def mouseDownEventGame(self, event):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      for piece in self.pieces:
        piece.setActive(pos)

  def mouseUpEventGame(self, event):
    if event.type == pygame.MOUSEBUTTONUP:
      for piece in self.pieces:
        piece.place()
    
  def mouseMoveEventGame(self, event):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      for piece in self.pieces:
        piece.move(pos)
      
  def game(self, event):
    self.mouseDownEventGame(event)
    self.mouseUpEventGame(event)
    self.mouseMoveEventGame(event)

  def main_menu(self):
    pass
