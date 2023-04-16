class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]





if __name__ == "__main__":

  class Logger(metaclass=Singleton):
    def __init__(self) -> None:
        self.x = 5


  a = Logger()
  b = Logger()
  c = Logger()
  print(a, b, c)