from pathlib import Path as path


CURRENTDIR = path.cwd().joinpath('code')
IMGPATH = CURRENTDIR.joinpath('Images')


# Board values
SQUAREWIDTH = 74
SQUAREHEIGHT = 74
BOARDLEFT = 137
BOARDRIGHT = BOARDLEFT + 8*SQUAREWIDTH
BOARDTOP = 54
BOARDBOTTOM = 646


# UTILS
def is_even(num: int):
    if num % 2 == 0:
        return True
    return False


def is_inside_board(pos):
    if BOARDLEFT < pos[0] < BOARDRIGHT \
            and BOARDTOP < pos[1] < BOARDBOTTOM:
        return True


def filter_none(squares):
    return list(filter(lambda square: square is not None, squares))


def filter_empty(squares):
    return list(filter(lambda square: square != "", squares))


def get_enemy_color(color):
    if color == "WHITE":
        return "BLACK"
    else:
        return "WHITE"


def file_distance(square, new_square):
    files = "abcdefgh"
    square_file = files.index(square[0])
    new_square_file = files.index(new_square[0])
    return new_square_file - square_file

def row_distance(square, new_square):
    old_row = int(square[1])
    new_row = int(square[1])
    return abs(new_row - old_row)


# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# COLUMNS IN TABLE
COLOR = 0
PIECENAME = 1

# COORDINATES
X = 0
Y = 1

# WINDOW VARIABLES
SWP_NOMOVE = 0x0002
SWP_NOOWNERZORDER = 0x0200
SWP_NOSIZE = 0x0001

#GET NEW SQUARES

UP = 8
DOWN = 8

LEFT = 1
RIGHT = 1

RIGHTUP = 9
RIGHTDOWN = 7
LEFTUP = 7
LEFTDOWN = 9

#SQUARE INDICES 

A1 = 0
B1 = 1
C1 = 2
D1 = 3
E1 = 4
F1 = 5
G1 = 6
H1 = 7
A2 = 8
B2 = 9
C2 = 10
D2 = 11
E2 = 12
F2 = 13
G2 = 14
H2 = 15
A3 = 16
B3 = 17
C3 = 18
D3 = 19
E3 = 20
F3 = 21
G3 = 22
H3 = 23
A4 = 24
B4 = 25
C4 = 26
D4 = 27
E4 = 28
F4 = 29
G4 = 30
H4 = 31
A5 = 32
B5 = 33
C5 = 34
D5 = 35
E5 = 36
F5 = 37
G5 = 38
H5 = 39
A6 = 40
B6 = 41
C6 = 42
D6 = 43
E6 = 44
F6 = 45
G6 = 46
H6 = 47
A7 = 48
B7 = 49
C7 = 50
D7 = 51
E7 = 52
F7 = 53
G7 = 54
H7 = 55
A8 = 56
B8 = 57
C8 = 58
D8 = 59
E8 = 60
F8 = 61
G8 = 62
H8 = 63