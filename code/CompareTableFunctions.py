from SquareTableNewApproach import SquareTableNewApproach
from SquareTableNumpy import SquareTableNumpy
from CheckForChecksNewApproach import CheckForChecksNewApproach
from CheckForChecksNumpy import CheckForChecksNumpy
import timeit
from config import *

class Compare():
    
    def __init__(self):
        self.table = SquareTableNumpy()
        self.table_new = SquareTableNewApproach()
        self.check = CheckForChecksNumpy()
        self.check_new = CheckForChecksNewApproach()
        self.table = self.table.squareTableNumpy
        self.table_new = self.table_new.squareTableNumpy
        self.color = 'WHITE'
        self.side = 'king_side'

    def getMethods(self, object):
        object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]
        print(object_methods)


    def execMethod1(self):
        self.check.is_in_check('WHITE', self.table)

    def execMethod2(self):
        self.check_new.is_in_check('WHITE', self.table_new)

        
    def compare(self):
        print(f"EXEC METHOD 1 FINSIHED IN: ")
        print(timeit.timeit('Compare().execMethod1()', setup='from __main__ import Compare', number=100000))
        print(f"EXEC METHOD 2 FINSIHED IN: ")
        print(timeit.timeit('Compare().execMethod2()', setup='from __main__ import Compare', number=100000))


if __name__ == "__main__":
    c = Compare()

    c.compare()
    
    # print(timeit.timeit('c.execMethod1', setup='from __main__ import c', number=1000000))
    # print(timeit.timeit('c.execMethod2', setup='from __main__ import c', number=1000000))