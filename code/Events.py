from GameEvents import GameEvents
from MainMenuEvents import MainMenuEvents
from MainMenu import MainMenu

class Events:

    def __init__(self):
        self.GameEvents = GameEvents
        self.MainMenu = MainMenu
        self.events_collection = dict()
        self.map_event('game', self.GameEvents)
        self.map_event('main_menu', self.MainMenu)

    def map_event(self, name, cls):
        self.events_collection[name] = cls

    def loadEvents(self, view, event):
        return self.events_collection[view]().events(event)
