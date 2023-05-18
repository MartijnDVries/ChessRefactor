from SquareTable import SquareTable
from Position import Position
from CheckForChecks import CheckForChecks


from Moves import LegalMoves
from MovesNumpy import LegalMovesNumpy
import timeit
from config import *

class Compare():
    
    def __init__(self):
        self.positionHandler = Position()
        self.table_new = SquareTable()
        self.check_new = CheckForChecks()
        self.moves = LegalMoves()
        self.moves_new = LegalMovesNumpy()
        self.position = self.positionHandler.position
        self.table_new = self.table_new.squareTable
        self.color = 'WHITE'
        self.side = 'king_side'

    def getMethods(self, object):
        object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]
        print(object_methods)


    def execMethod1(self):
        self.moves.moves_list(self.table_new, 'WHITE')

    def execMethod2(self):
        self.moves_new.moves_list(self.table, 'WHITE')

        
    def compare(self):
        print(f"METHOD 1 FINSIHED IN: ")
        print(timeit.timeit('Compare().execMethod1()', setup='from __main__ import Compare', number=1000))
        print(f"METHOD 2 FINSIHED IN: ")
        print(timeit.timeit('Compare().execMethod2()', setup='from __main__ import Compare', number=1000))


if __name__ == "__main__":
    c = Compare()

    c.compare()
    
    # print(timeit.timeit('c.execMethod1', setup='from __main__ import c', number=1000000))
    # print(timeit.timeit('c.execMethod2', setup='from __main__ import c', number=1000000))