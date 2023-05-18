import pygame
from config import *
from Image import Image


class Piece(pygame.sprite.Sprite):

  def __init__(self, image_file, color, square, position, name):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.color = color
    self.square = square
    self.image = Image(image_file)
    self.rect = self.image.rect
    self.rect.center = position
    self.original_position = position
    self.active = False
    self.placed = True

  def __repr__(self):
    return f"{self.color} {self.name.lower()} on {self.square}  POS: {self.rect.center}\n"

  def setActive(self, pos):
    if self.rect.collidepoint(pos):
      self.active = True

  def dragTo(self, pos):
    if self.active:
      self.rect.center = (pos[0], pos[1])

  def place(self):
    if self.active:
      self.active = False

  def update(self, new_pos, new_square):
    self.rect.center = new_pos
    self.original_position = new_pos
    self.square = new_square

  def placeback(self):
    self.rect.center = self.original_position
    
  def draw(self, surface):
    surface.blit(self.image.image, self.rect)



