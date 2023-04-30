from Location import Location
from SquareName import SquareName
from Color import Color
from PieceName import PieceName
from typing import Optional

class Square:
    def __init__(self, location, name, piece_color: Optional[str] = None, piece_name: Optional[str] = None):
        self.location = Location(*location)
        self.color = Color(piece_color)
        self.square_name =  SquareName(name)
        self.piece = PieceName(piece_name)

    def __str__(self):
        return f"{self.square_name}: {self.color} {self.piece}"
    

    


if __name__ == "__main__":
    print(Square((100, 100), 'e1'))