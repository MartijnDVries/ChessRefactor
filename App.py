from Renderer import Render
from config import *
from Board import ChessBoard


class App:
    def __init__(self) -> None:
        self.Renderer = Render()
        self.board = ChessBoard()

    def run(self, view='game'):
        self.Renderer.setWindow(175, 0)
        self.Renderer.setBackground(RED)
        self.boardColor(black=(120, 17, 17))
        self.Renderer.render(view)

    def boardColor(self, white=WHITE, black=BLACK):
        self.board.setSquareColor(white, black)


if __name__ == "__main__":
    app = App()
    app.run()
