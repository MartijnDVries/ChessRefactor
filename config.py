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

#COLORS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)




