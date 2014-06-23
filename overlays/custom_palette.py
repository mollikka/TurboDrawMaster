import pygame
import colorsys

from overlay import Overlay, Button
from overlays.color_picker import ActiveColorButton

class CustomPaletteOverlay(Overlay):

    def __init__(self, user):
        super(CustomPaletteOverlay,self).__init__(user)
        self.name = "Custom Palette"

        for i in range(30):
            for j in range(15):
                self.buttons.append([CustomColorButton(self),(100+i*20,100+j*20)])
        self.buttons.append([ActiveColorButton(self),(0,100)])

class CustomColorButton(Button):

    def __init__(self, color_picker_overlay):
        self.rect = pygame.Rect((0,0),(18,18))
        self.texture = pygame.Surface((18,18))
        self.parent = color_picker_overlay
        self.color = (128,128,128)

    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            self.parent.user.active_color = self.color

    def right_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            self.color = self.parent.user.active_color

    def draw(self):
        self.texture.fill(self.color)
        return self.texture
