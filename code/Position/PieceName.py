class PieceName(str):
    def __new__(self, name):
        self.name = name
        return str.__new__(PieceName, self.name)
    
