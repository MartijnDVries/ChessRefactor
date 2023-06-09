from config import *
from PieceCollection import PieceCollection
from Board import ChessBoard
from Game import Game
from MainMenu import MainMenu


class Viewer:
    def __init__(self, surface):
        self.surface = surface
        self.board = ChessBoard()
        self.piecesInstance = PieceCollection()
        self.pieces = self.piecesInstance.pieceCollection
        self.Game = Game()

    def get_view(self):
        if self.Game.quit:
            return 'main_menu'
        else:
            return 'game'

    def view(self, view, surface):
        self.surface = surface
        if view == "main_menu":
            if not hasattr(self, 'main_mnu'):
                width, height = self.surface.get_width(), self.surface.get_height()
                self.main_mnu = MainMenu()
                self.main_mnu.set_surface(0, 0, width, height)
                self.main_mnu.set_bg_color(WHITE)
            self.main_menu()
        else:
            self.game()

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
