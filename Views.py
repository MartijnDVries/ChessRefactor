from config import *
from PieceCollection import PieceCollection
from Board import ChessBoard
from Game import Game
from MainMenu import MainMenu

class Viewer:
  def __init__(self, surface):
    self.surface = surface
    self.viewCollection = {'game': self.game, 'main_menu': self.main_menu}
    self.board = ChessBoard()
    self.piecesInstance = PieceCollection()
    self.pieces = self.piecesInstance.pieceCollection
    self.Game = Game()
    width, height = self.surface.get_width(), self.surface.get_height()
    self.main_mnu = MainMenu(0, 0, width, height, WHITE, 'bg-image.jpg')

  def view(self, view):
    return self.viewCollection[view]()
    
  def main_menu(self):
    self.main_mnu.draw(self.surface)

  def game(self):
    self.board.draw(self.surface)
    for piece in self.pieces:
      if not piece.active:
        piece.draw(self.surface)
    if any((active_piece := piece) for piece in self.pieces if piece.active):
      active_piece.draw(self.surface)


if __name__ == "__main__":
  pass
