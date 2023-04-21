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
  

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#COLUMNS IN TABLE
POSITION = 0
OCCUPIED = 1
COLOR = 2
PIECENAME = 3

#WINDOW VARIABLES
SWP_NOMOVE = 0x0002
SWP_NOOWNERZORDER = 0x0200
SWP_NOSIZE = 0x0001
