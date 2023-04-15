from config import *
from Container import *


class Viewer:
  def __init__(self, surface):
    self.surface = surface
    self.viewCollection = {'game': self.game, 'main_menu': self.main_menu}

  def view(self, view):
    return self.viewCollection[view]()
    

  def main_menu(self):
    pass

  def game(self):
    ServiceContainer.board.draw(self.surface)
    for piece in ServiceContainer.pieceCollection:
      piece.draw(self.surface)
    



if __name__ == "__main__":
  pass
