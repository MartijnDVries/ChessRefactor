from SquareTable import SquareTable
from Position import Position
import timeit
import ujson
from copy import deepcopy


class TimeIt:
    def __init__(self):
        self.s = SquareTable()
        self.p = Position()

    def copy_squaretable(self):
        table = ujson.loads(ujson.dumps(self.s.squareTable))

    def copy_position(self):
        table = self.p.copy()



if __name__ == "__main__":
    print(timeit.timeit('TimeIt().copy_squaretable()', setup='from __main__ import TimeIt', number=100000))
    print(timeit.timeit('TimeIt().copy_position()', setup='from __main__ import TimeIt', number=100000))