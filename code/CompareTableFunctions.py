from SquareTableNumpy import SquareTableNumpy
from SquareTable import SquareTable
from CheckForChecks import CheckForChecks
from CheckForChecksNumpy import CheckForChecksNumpy
import timeit
from config import *

class Compare():
    
    def __init__(self):
        self.table = SquareTable()
        self.numpy_table = SquareTableNumpy()
        self.check = CheckForChecks()
        self.numpy_check = CheckForChecksNumpy()
        self.table_normal = self.table.squareTable
        self.table_numpy = self.numpy_table.squareTableNumpy
        self.color = 'WHITE'
        self.side = 'king_side'

    def getMethods(self, object):
        object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]
        print(object_methods)


    def execMethod1(self):
        self.check.is_in_check('WHITE', self.table_normal)
        
    def execMethod2(self):
        self.numpy_check.is_in_check('WHITE', self.table_numpy)

        

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