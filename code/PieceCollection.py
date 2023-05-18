from config import *
from ChessPiece import Piece
from Singleton import Singleton
from start_position import StartPos
from Coordinates import Coordinates

class PieceCollection(metaclass=Singleton):


    def __init__(self):
        self.table = StartPos().startpos
        self.piece_coordinates = Coordinates().coordinates
        self.pieceCollection = self.getCollection()


    def parseImageFile(self, piece, color):
        image_file = f"{color.lower()}_{piece.lower()}"
        return image_file
    
    
    def getPosition(self, square):
        return self.piece_coordinates[square]


    def getCollection(self):
        pieceCollection = []
        for square_index, square in enumerate(self.table):
            if square[PIECENAME]:
                pieceCollection.append(
                    Piece(
                    self.parseImageFile(square[PIECENAME], square[COLOR]),
                    square[COLOR],
                    square_index, 
                    self.getPosition(square_index),
                    square[PIECENAME])
                    )
        return pieceCollection
    
    
    def getPiece(self, square):
        if any((get_piece := piece) for piece in self.pieceCollection if piece.square == square):
            return get_piece


    def delete(self, piece):
        self.pieceCollection.remove(piece)
        del piece
        

    def update(self, square):
        if any((remove_piece := piece) for piece in self.pieceCollection if piece.square == square):
            self.delete(remove_piece)


if __name__ == "__main__":
    p = PieceCollection()
