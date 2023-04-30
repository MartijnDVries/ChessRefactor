import operator


class Location(tuple):
  def __new__ (self, x, y):
     return tuple.__new__(Location, (x, y))

Location.x = property(operator.itemgetter(0))
Location.y = property(operator.itemgetter(1))
    
    
if __name__ == "__main__":
    pass
   