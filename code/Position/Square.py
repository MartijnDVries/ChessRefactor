from Location import Location
from SquareName import SquareName
from Color import Color
from PieceName import PieceName
import Errors
from typing import Optional

class Square:
    def __init__(self, location, name, piece_color: Optional[str] = None, piece_name: Optional[str] = None):
        self.location = Location(*location)
        self.square_name = name
        if piece_color:
            self.color = Color(piece_color)
        else:
            self.color = None
        if piece_name:
            self.piece = PieceName(piece_name)
        else:
            self.piece = None

    def __str__(self):
        return f"{self.square_name}: {self.color} {self.piece}"
    
    
    def hasPiece(self, piecename):
        if isinstance(self.piece, PieceName) and self.piece == piecename:
            return True
    
        return False
    
    def hasColor(self, color):
        if isinstance(self.color, Color) and self.color == color:
            return True
        
        return False
    
    def hasPieceAndColor(self, piecename, color):
        if self.hasPiece(piecename) and self.hasColor(color):
            return True
        
        return False
        
    
    def has(self, color=None, piece=None):
        if piece and not color:
            return self.hasPiece(piece)
        if piece and color:
            return self.hasPieceAndColor(piece, color)
        if color and not piece:
            return self.hasColor(color)
        else: raise Errors.TooFewArgumentsExecption("This function needs at least one argument")

    


if __name__ == "__main__":
    
    s1 = Square((100, 100), 'e1', 'WHITE', 'KING') 
    s2 = Square((100, 100), 'd1')
    print(s1.square_name)
    print(s1.hasPiece('KING'))
    print(s1.has("WHITE", "KING"))