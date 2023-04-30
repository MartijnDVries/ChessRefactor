from Square import Square
from SquareName import SquareName
from Color import Color
from PieceName import PieceName

class Position:

    def __init__(self, squares: list[Square]):
        self.squares = squares


    def has_piece(self, square_name, piece_name=None):
        if piece_name:
          if self.squares[Square.square_name] == piece_name:
            return True
        else:
           return False



if __name__ == "__main__":
    start_pos = [
        Square((100, 100), 'e1', 'WHITE', 'KING'), 
        Square((100, 100), 'd1', 'WHITE', 'ROOK'), 
        Square((100, 100), 'c1', 'WHITE', 'KNIGHT'), 
        Square((100, 100), 'f1', 'WHITE', 'QUEEN')
        ]
    
    p = Position(start_pos)

    print(p.has_piece('e1', 'KING'))