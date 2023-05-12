from config import *

class Coordinates:
     
    def __init__(self):
        self.piece_coordinates = self.getPieceCoordinates()

    def getPieceCoordinates(self):
        """Center X, Y for all squares attached to squarename"""
        coordinates = dict()
        chars = "abcdefgh"
        start_x = BOARDLEFT + (SQUAREWIDTH // 2)
        y = BOARDBOTTOM + (SQUAREHEIGHT // 2)
        for row in range(1, 9):
            x = start_x
            y -= SQUAREHEIGHT
            for col in chars:
                x += SQUAREWIDTH
                square = col + str(row)
                coordinates[square] = (x, y)
        return coordinates
    

if __name__ == "__main__":
    c = Coordinates()
    c.getPieceCoordinates()