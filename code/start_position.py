import numpy as np

class StartPos:
    
    def __init__(self) -> None:
        self.startpos = dict()
        self.setSquareNames()
        self.setColor()
        self.setPieces()
        self.startposNumpy = np.array([[]])
        self.setSquareNamesNumpy()

    def setSquareNames(self):
        """Center X, Y for all squares attached to squarename"""
        chars = "abcdefgh"
        for row in range(1, 9):
            for col in chars:
                square = col + str(row)
                self.startpos[square] = []

    def setColor(self):
        """Set default color on the squares"""
        for square in self.startpos:
            row = int(square[1])
            if row == 1 or row == 2:
                self.startpos[square].append("WHITE")
            elif row == 7 or row == 8:
                self.startpos[square].append("BLACK")
            else:
                self.startpos[square].append("")

    def setPieces(self):
        """Set up starting position"""
        for square in self.startpos:
            row = int(square[1])
            file = square[0]
            if row == 7 or row == 2:
                self.startpos[square].append("PAWN")
                continue
            elif row == 1 or row == 8:
                if file == 'a' or file == 'h':
                    self.startpos[square].append("ROOK")
                    continue
                elif file == 'b' or file == 'g':
                    self.startpos[square].append("KNIGHT")
                elif file == 'c' or file == 'f':
                    self.startpos[square].append("BISHOP")
                elif square == 'e1':
                    self.startpos[square].append("KING")
                elif square == 'e8':
                    self.startpos[square].append("KING")
                elif square == 'e8':
                    self.startpos[square].append("KING")
                elif square == 'd1':
                    self.startpos[square].append("QUEEN")
                elif square == 'd8':
                    self.startpos[square].append("QUEEN")
            else:
                self.startpos[square].append("")

    def setSquareNamesNumpy(self):
        """Center X, Y for all squares attached to squarename"""
        chars = "abcdefgh"
        for row in range(1, 9):
            for col in chars:
                square = col + str(row)
                if np.size(self.startposNumpy) == 0:
                    self.startposNumpy = np.array(
                        [[self.setColorNumpy(row),  self.setPiecesNumpy(row, col)]])
                else:
                    self.startposNumpy = np.append(self.startposNumpy, 
                        [[self.setColorNumpy(row),  self.setPiecesNumpy(row, col)]], axis=0)

    def setColorNumpy(self, row):
        """Set default color on the squares"""
        if row == 1 or row == 2:
            return 'WHITE'
        elif row == 7 or row == 8:
            return 'BLACK'
        else:
            return ''

    def setPiecesNumpy(self, row , file):
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

    print(s.startposNumpy)


    s2 = np.copy(s.startposNumpy)

    s2[63] = ['', '', '']

    print("S1---------------------------------------------")
    print(s.startposNumpy)

    print("S2---------------------------------------------")
    print(s2)