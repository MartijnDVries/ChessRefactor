
import pygame
from config import *
from Image import Image
from Game import Game
from MainMenuButtons import MainMenuButtons


class MainMenu():
    
    def __init__(self):
       self.buttons = MainMenuButtons().buttonCollection

    def set_surface(self,  x, y, width, height):
       self.rect = pygame.Rect(x, y, width, height)
       
    def set_bg_image(self, image_file):
        self.image = Image(image_file)
        self.image.image = pygame.transform.scale(self.image.image, (self.rect.width, self.rect.height))

    def set_bg_color(self, color):
       self.color = color
             
    def draw(self, surface):
      surface.fill(self.color)
      if hasattr(self, 'image'):
        surface.blit(self.image.image, self.rect)
      for button in self.buttons.values():
         button.draw(surface)

    def events(self, event):
       pass
    