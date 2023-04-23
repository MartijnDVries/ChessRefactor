import pygame
from config import *
from Image import Image
from Game import Game

class MainMenu(pygame.Surface):
    def __init__(self, x, y, width, height, color, image_file=None):
        pygame.Surface.__init__(self, size=(width, height))
        self.color = color
        if image_file:
            self.image = Image(image_file)
            self.image.image = pygame.transform.scale(self.image.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)




    def draw(self, surface):
      if hasattr(self, 'image'):
        surface.blit(self.image.image, self.rect)
        return
      self.fill(self.color)
      surface.blit(self, self.rect)
        