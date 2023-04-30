class SquareName(str):
    
    def __new__(self, square_name):
        self.square_name = square_name
        return str.__new__(SquareName, square_name)
    

if __name__ == "__main__":
    print(SquareName('a1'))