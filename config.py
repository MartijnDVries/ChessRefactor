import os

CURRENTDIR = os.getcwd()
IMGPATH = CURRENTDIR + '\\Images\\'

# Board values
SQUAREWIDTH = 74
SQUAREHEIGHT = 74
BOARDLEFT = 174
BOARDRIGHT = 766
BOARDTOP = 54
BOARDBOTTOM = 646



#UTILS
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

def get_enemy_color(color):
   if color == "WHITE":
      return "BLACK"
   else:
      return "WHITE"
   
def file_distance(square, new_square):
   files = "abcdefgh"
   square_file = files.index(square[0])
   new_square_file = files.index(new_square[0])
   return abs(new_square_file - square_file)
  

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#COLUMNS IN TABLE
POSITION = 0
# OCCUPIED = 1
COLOR = 1
PIECENAME = 2

#WINDOW VARIABLES
SWP_NOMOVE = 0x0002
SWP_NOOWNERZORDER = 0x0200
SWP_NOSIZE = 0x0001
