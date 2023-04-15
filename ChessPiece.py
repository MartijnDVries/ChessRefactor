import pygame
from config import *


class Piece(pygame.sprite.Sprite):

  def __init__(self, image_file, color, square, position):
    pygame.sprite.Sprite.__init__(self)
    self.color = color
    self.square = square
    self.image = pygame.image.load(IMGPATH + image_file + ".png")
    self.rect = self.image.get_rect()
    self.rect.center = position
    self.active = False
    self.placed = True


  def get_middle():
    pass

  
  def move(self, event, surface):
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.rect.collidepoint(pos):
        self.active = True
    if self.active:
      if BOARDLEFT < pos[0] < BOARDRIGHT \
          and BOARDTOP < pos[1] < BOARDBOTTOM:
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    if event.type == pygame.MOUSEBUTTONUP:
      self.active = False


  def draw(self, surface):
    surface.blit(self.image, self.rect)

