from Button import Button


class MainMenuButtons:

    def __init__(self):
        self.buttonCollection = dict()
        self.buttons()

    def buttons(self):
        self.buttonCollection['start'] = Button(100, 100, 100, 50, (0, 255, 0), (0, 210, 0), text='Start')
        self.buttonCollection['stop'] = Button(100, 250, 100, 50, (255, 0, 0), (210, 0, 0), text='Stop')


    # def start_stop_switcher(self):
    #     start_stop_switcher = Switcher()


if __name__ == "__main__":
    m = MainMenuButtons()
    m.buttons()
    print(m.buttonCollection)