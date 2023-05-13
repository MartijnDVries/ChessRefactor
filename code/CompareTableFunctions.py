from SquareTableNumpy import SquareTableNumpy
from SquareTable import SquareTable
import timeit
from config import *

class Compare():
    
    def __init__(self):
        self.table = SquareTable()
        self.numpy_table = SquareTableNumpy()
        self.t = self.table.squareTable

    def getMethods(self, object):
        object_methods = [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]
        print(object_methods)


    def execMethod1(self):
        if self.t['e1'][PIECENAME] == 'KING':
            print("YES")

    def execMethod2(self):
        if self.table.hasPiece('e1', 'KING'):
            print("YES")
        


if __name__ == "__main__":
    c = Compare()

    print(timeit.timeit('c.execMethod1', 'from __main__ import c', number=10000000))
    print(timeit.timeit('c.execMethod2', 'from __main__ import c', number=10000000))