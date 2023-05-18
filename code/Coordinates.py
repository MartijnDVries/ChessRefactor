from config import *

class Coordinates:
     
    def __init__(self):
        self.coordinates = self.getPieceCoordinates()

    def getPieceCoordinates(self):
        """Center X, Y for all squares attached to squarename"""
        coordinates = dict()
        chars = "abcdefgh"
        start_x = (BOARDLEFT + (SQUAREWIDTH // 2)) - SQUAREWIDTH
        y = BOARDBOTTOM + (SQUAREHEIGHT // 2)
        index  = 0
        for row in range(1, 9):
            x = start_x
            y -= SQUAREHEIGHT
            for col in chars:
                x += SQUAREWIDTH
                square = col + str(row)
                coordinates[index] = (x, y)
                index += 1
        return coordinates
    
    def getSquareFromCoordinates(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]

        index = list(filter(lambda square: self.coordinates[square][X] 
            in range( pos_x - (SQUAREWIDTH // 2), pos_x + (SQUAREWIDTH // 2))
            and self.coordinates[square][Y] in range(pos_y - (SQUAREHEIGHT // 2), pos_y + ((SQUAREHEIGHT // 2))), 
            self.coordinates))
        
        return index[0]
    

if __name__ == "__main__":
    c = Coordinates()
    c.getPieceCoordinates()
