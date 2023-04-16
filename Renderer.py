import pygame
import os
from Background import BackGroundImage
from config import *
from Views import Viewer
from Events import EventChecker


class Render:

  def __init__(self, x, y):
    pygame.init()
    self.windowPos = os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    self.events = None
    self.view = None
    self.display = pygame.display.set_mode((1, 1))
    self.background_image = None
    self.background_color = None
    self.Viewer = Viewer(self.display)
    self.Events = EventChecker()
    self.clock = pygame.time.Clock()
    self.run = True
    

  def loadView(self, view):
    self.Viewer.view(view)

  def updateView(self, view):
    self.renderBackground()
    self.Viewer.view(view)
    

  def eventLoader(self, view, event):
    """Load the events of the corresponding view"""
    self.Events.loadEvents(view, event)

  def setScreen(self, width, height):
    """Set screen width and height"""
    self.display = pygame.display.set_mode((width, height))

  def setBackground(self, color=[255, 255, 255], image=None):
    """Set background color or image"""
    self.background_color = color
    if image:
      self.background_image = BackGroundImage(image, [0, 0])

  def renderBackground(self):
    self.display.fill(self.background_color)
    if self.background_image:
      self.display.blit(self.background_image.image, self.background_image.rect)
      return
    
  def removeBgImage(self):
    """Set background image to None"""
    self.background_image = None

  def render(self, view):
    self.loadView(view)
    while self.run:
      self.clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
        self.eventLoader(view, event)
      self.updateView(view)
      pygame.display.flip()



if __name__ == "__main__":
  r = Render(275, 30)
  r.setScreen(1000, 700)
  r.setBackground(RED)
  r.render('game')

  