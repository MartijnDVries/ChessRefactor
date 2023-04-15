import pygame
import os
from Background import BackGroundImage
from config import *
from Views import Viewer



class RenderGame:

  def __init__(self, x, y):
    pygame.init()
    self.windowPos = os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    self.events = None
    self.view = None
    self.display = pygame.display.set_mode((1, 1))
    self.background = None
    self.Viewer = Viewer(self.display)
    self.clock = pygame.time.Clock()
    self.run = True
    

  def loadView(self, view):
    self.Viewer.view(view)

  def updateView(self, view):
    self.Viewer.view(view)

  def eventLoader(self, events):
    raise NotImplementedError("Not implemented yet")

  def setScreen(self, width, height):
    self.display = pygame.display.set_mode((width, height))

  def setBackground(self, color=[255, 255, 255], image=None):
    if image: 
      img = BackGroundImage(image, [0, 0])
      self.display.blit(img.image, img.rect)
      return

    self.display.fill(color)
    pygame.display.update()
      


  def render(self, view):

    self.loadView(view)
    
    while self.run:
      self.clock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
       

      self.updateView(view)
      pygame.display.flip()



if __name__ == "__main__":
  r = RenderGame(275, 30)
  r.setScreen(1000, 700)
  r.setBackground(RED)
  r.render('game')

  