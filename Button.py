import pygame


class Button:

    def __init__(self, x, y, width, height, btn_color, click_btn_color, active_btn_color=None, border_radius=5,
                 font="Arial", font_size=24, text='', textcolor=(0, 0, 0)):
        """Class to create buttons with different aspects of this button"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(font, font_size)
        self.text = text
        self.textcolor = textcolor
        self.border_radius = border_radius
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.btn_color = btn_color
        self.active_btn_color = click_btn_color


    def draw(self, surface):
        """when all info is collected in init method draw button on the screen, also blit text in center of button"""
        if self.active:
            color = self.active_btn_color
        else:
            color = self.btn_color
        pygame.draw.rect(surface, color, self.rect, border_radius=self.border_radius)
        text_surf = self.font.render(self.text, True, self.textcolor)
        surface.blit(text_surf, (self.x + (self.width / 2 - text_surf.get_width() / 2),
                          self.y + (self.height / 2 - text_surf.get_height() / 2)))

    def button_clicked(self):
        """function call when button is clicked. It changes te color of the button"""
        if self.active:
            self.active = False
        else:
            self.active = True