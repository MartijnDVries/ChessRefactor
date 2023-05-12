class FEN:
    
    def __init__(self):
       self.startPosition  = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    

    def read(self, fen_string):
        pass
    


if __name__ == "__main__":
    f = FEN()
    print(f.startPosition[5])

    # new_pos = f.startPosition[5] = "n"

    # print(new_pos)

    # print(f.startPosition)
        
