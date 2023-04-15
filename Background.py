import pygame
import config


class BackGroundImage(pygame.sprite.Sprite):

  def __init__(self, image_file, location):
    pygame.sprite.Sprite.__init__(self)
    self.path = config.IMGPATH + image_file
    self.image = pygame.image.load(self.path)
    self.rect = self.image.get_rect()
    self.rect.left, self.rect.top = location
     
  
if __name__ == "__main__":
  BackGroundImage('bg-image.jpg', [0, 0])