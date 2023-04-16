from config import *
from PieceCollection import PieceCollection
from Board import ChessBoard


class Viewer:
  def __init__(self, surface):
    self.surface = surface
    self.viewCollection = {'game': self.game, 'main_menu': self.main_menu}
    self.board = ChessBoard()
    self.piecesInstance = PieceCollection()
    self.pieces = self.piecesInstance.pieceCollection

  def view(self, view):
    return self.viewCollection[view]()
    
  def main_menu(self):
    pass

  def game(self):
    self.board.draw(self.surface)
    for piece in self.pieces:
      piece.draw(self.surface)

if __name__ == "__main__":
  pass
