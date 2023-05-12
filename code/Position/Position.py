from Square import Square
from copy import deepcopy, copy

class Position:

    def __init__(self):
        self.squares = self.setStartPos()
        self.square_name_list = [str(x + str(y)) for x in 'abcdefgh' for y in range(1, 9)]


    def __call__(cls, square_name):
      if square_name in cls.square_name_list:
        return cls.squares[cls.square_name_list.index(square_name)]
      else: 
         raise IndexError("Square not found in position")
 
    def setStartPos(self):
       return [
        Square((100, 100), 'a1', 'WHITE', 'ROOK'),
        Square((100, 100), 'a2', 'WHITE', 'KNIGHT'), 
        Square((100, 100), 'a3'), 
        Square((100, 100), 'a4'), 
        Square((100, 100), 'a5'), 
        Square((100, 100), 'a6'), 
        Square((100, 100), 'a7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'a8', 'BLACK', 'ROOK'),
        Square((100, 100), 'b1', 'WHITE', 'KNIGHT'),
        Square((100, 100), 'b2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'b3'), 
        Square((100, 100), 'b4'), 
        Square((100, 100), 'b5'), 
        Square((100, 100), 'b6'), 
        Square((100, 100), 'b7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'b8', 'BLACK', 'KNIGHT'),
        Square((100, 100), 'c1', 'WHITE', 'BISHOP'),
        Square((100, 100), 'c2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'c3'), 
        Square((100, 100), 'c4'), 
        Square((100, 100), 'c5'), 
        Square((100, 100), 'c6'), 
        Square((100, 100), 'c7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'c8', 'BLACK', 'BISHOP'),
        Square((100, 100), 'd1', 'WHITE', 'QUEEN'),
        Square((100, 100), 'd2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'd3'), 
        Square((100, 100), 'd4'), 
        Square((100, 100), 'd5'), 
        Square((100, 100), 'd6'), 
        Square((100, 100), 'd7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'd8', 'BLACK', 'QUEEN'),
        Square((100, 100), 'e1', 'WHITE', 'KING'),
        Square((100, 100), 'e2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'e3'), 
        Square((100, 100), 'e4'), 
        Square((100, 100), 'e5'), 
        Square((100, 100), 'e6'), 
        Square((100, 100), 'e7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'e8', 'BLACK', 'KING'),
        Square((100, 100), 'f1', 'WHITE', 'BISHOP'),
        Square((100, 100), 'f2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'f3'), 
        Square((100, 100), 'f4'), 
        Square((100, 100), 'f5'), 
        Square((100, 100), 'f6'), 
        Square((100, 100), 'f7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'f8', 'BLACK', 'BISHOP'),
        Square((100, 100), 'g1', 'WHITE', 'KNIGHT'),
        Square((100, 100), 'g2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'g3'), 
        Square((100, 100), 'g4'), 
        Square((100, 100), 'g5'), 
        Square((100, 100), 'g6'), 
        Square((100, 100), 'g7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'g8', 'BLACK', 'KNIGHT'),
        Square((100, 100), 'h1', 'WHITE', 'ROOK'),
        Square((100, 100), 'h2', 'WHITE', 'PAWN'), 
        Square((100, 100), 'h3'), 
        Square((100, 100), 'h4'), 
        Square((100, 100), 'h5'), 
        Square((100, 100), 'h6'), 
        Square((100, 100), 'h7', 'BLACK', 'PAWN'), 
        Square((100, 100), 'h8', 'BLACK', 'ROOK'),  
        ]
    
    def copy(self):
       return self
       
    def setMove(self):
       self.squares[0].piece = self.squares[1].piece
       self.squares[0].color = self.squares[1].color



if __name__ == "__main__":
    
    
    p = Position()

    p2 = p.copy()
    print(p('a1').has('WHITE', 'ROOK'))
    print(p2('a1').has('WHITE', 'ROOK'))


    p.setMove()
    print(p('a1').has('WHITE', 'ROOK'))
    print(p('a1').has('WHITE', 'ROOK'))


    
    print(id(p), id(p2))
