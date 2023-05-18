import random
from Singleton import Singleton

PIECENAME = 1
COLOR = 0

class Chain():
    def __init__(self, piece, square, color) -> None:
        self.square = square
        if piece:
          self.piece = piece
          self.test_dict[square][PIECENAME] = piece
        if color:
            self.color = color
            self.test_dict[square][COLOR] = color
    
    def __repr__(self) -> str:
        if self.test_dict[self.square][PIECENAME] == self.piece:
            return "TRUE"
        else: 
            return "FALSE"
        
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'test_dict'):
            piece_list = ["PAWN", "ROOK", "KING"]
            color_list = ["WHITE", "BLACK"]
            square_list = ["a1", "a2", "b1", "b2", "c1", "c2", "d1", "d2", "e1", "e2"]
            test_dict = dict()
            for i in square_list:
                test_dict[i] = [color_list[random.randint(0, 1)], piece_list[random.randint(0, 2)]]
            setattr(cls, 'test_dict', test_dict)
        return super().__new__(cls)


    def on(self, square):
        piece = self.piece
        color = self.color
        return type(self)(piece, square, color)
    
    def hasPiece(self, piece=""):
        square = self.square
        color = self.color
        if not piece:
            piece = self.piece
        return type(self)(piece, square, color)
        

if __name__ == "__main__":
    c = Chain("KING", "a1", "WHITE")
    print(c.test_dict)
    print(c.piece)
    c2 = Chain("ROOK", "b2", "BLACK")
    print(c2.test_dict)
    print(c2.piece)

    print(c2.hasPiece("KING").on("b2"))



