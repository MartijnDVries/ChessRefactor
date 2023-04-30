
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import pygame
from config import *
from Image import Image
from Location import Location
from SquareName import SquareName
from Color import Color



class Piece(pygame.sprite.Sprite):

  def __init__(self, image_file, color, square, location, name):
    pygame.sprite.Sprite.__init__(self)
    self.name = name
    self.color = Color(color)
    self.square = SquareName(square)
    self.image = Image(image_file)
    self.rect = self.image.rect
    self.rect.center = Location(location)
    self.original_position = Location(location)
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


if __name__ == "__main__":
  # piece = Piece('white_king', 'WHITE', 'a1', (100, 100), 'KING')
  p = Image('white_king')