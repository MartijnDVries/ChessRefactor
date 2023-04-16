import pygame
from config import *


class Piece(pygame.sprite.Sprite):

  def __init__(self, image_file, color, square, position, name):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.color = color
    self.square = square
    self.image = pygame.image.load(IMGPATH + image_file + ".png")
    self.rect = self.image.get_rect()
    self.rect.center = position
    self.active = False
    self.placed = True

  def __repr__(self):
    return f"{self.color} {self.name} on {self.square}  POS: {self.rect.center}"

  def get_middle():
    pass

  
  def setActive(self, pos):
    if self.rect.collidepoint(pos):
      self.active = True

  def move(self, pos):
    if self.active:
      self.rect.x = pos[0]
      self.rect.y = pos[1]

  def place(self):
    if self.active:
      self.active = False
      print(self)


  def draw(self, surface):
    surface.blit(self.image, self.rect)

