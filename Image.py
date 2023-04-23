import pygame
from config import *
from pathlib import Path as path

class Image(pygame.sprite.Sprite):

  def __init__(self, image_file, location=None):
    pygame.sprite.Sprite.__init__(self)
    self.image_file = image_file
    self.path = self.get_path()
    self.image = pygame.image.load(self.path)
    self.rect = self.image.get_rect()
    if location:
      self.rect.left, self.rect.top = location
     
  def get_path(self):
    if path.is_file(IMGPATH.joinpath(self.image_file).with_suffix('.jpg')):
        return IMGPATH.joinpath(self.image_file).with_suffix('.jpg')
    if path.is_file(IMGPATH.joinpath(self.image_file).with_suffix('.png')):
        return IMGPATH.joinpath(self.image_file).with_suffix('.png')
    
if __name__ == "__main__":
  Image('bg-image', [0, 0])