import numpy as np

class StartPos:
    
    def __init__(self) -> None:
        self.startpos = self.setSquareNames()


    def setSquareNames(self):
        """Center X, Y for all squares attached to squarename"""
        chars = "abcdefgh"
        init_array = True
        for row in range(1, 9):
            for col in chars:
                if init_array:
                    self.startposNumpy = np.array(
                        [[self.setColor(row),  self.setPieces(row, col)]])
                    init_array = False
                else:
                    self.startposNumpy = np.append(self.startposNumpy, 
                        [[self.setColor(row),  self.setPieces(row, col)]], axis=0)
                    
        return self.startposNumpy
    

    def setColor(self, row):
        """Set default color on the squares"""
        if row == 1 or row == 2:
            return 'WHITE'
        elif row == 7 or row == 8:
            return 'BLACK'
        else:
            return ''


    def setPieces(self, row , file):
        """Set up starting position"""
        square =  file + str(row)
        if row == 7 or row == 2:
            return 'PAWN'
        elif row == 1 or row == 8:
            if file == 'a' or file == 'h':
                return 'ROOK'
            elif file == 'b' or file == 'g':
                return 'KNIGHT'
            elif file == 'c' or file == 'f':
                return 'BISHOP'
            elif square == 'e1':
                return 'KING'
            elif square == 'e8':
                return 'KING'
            elif square == 'd1':
                return 'QUEEN'
            elif square == 'd8':
                return 'QUEEN'
        else:
            return ''

if __name__ == "__main__":
    s = StartPos()

    print(s.startpos)


    s2 = np.copy(s.startpos)

    s2[63] = ['', '']

    print("S1---------------------------------------------")
    print(s.startpos)

    print("S2---------------------------------------------")
    print(s2)