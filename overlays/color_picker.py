import pygame
import colorsys

from overlay import Overlay, Button

class ColorPickerOverlay(Overlay):

    def __init__(self, user):
        super(ColorPickerOverlay,self).__init__(user)
        self.name = "Color Picker"

        self.buttons.append([HueLumSurfaceButton(self),(100,100)])
        self.buttons.append([SatSliderButton(self),(750,100)])
        self.buttons.append([ActiveColorButton(self),(0,100)])

class HueLumSurfaceButton(Button):

    def __init__(self, color_picker_overlay):
        self.rect = pygame.Rect((0,0),(640,480))
        self.texture = self.build_color_map()
        self.parent = color_picker_overlay

    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            self.parent.user.active_color = self.coords_to_color(mouse_x,mouse_y)

    def coords_to_color(self, x, y):
        width,height = self.rect.size
        color = colorsys.hls_to_rgb(float(x)/width,float(y)/height,1)
        color = [i*255 for i in color]
        return color

    def build_color_map(self):
        width, height = self.rect.size
        colormap = pygame.Surface(self.rect.size)

        for x in range(width):
            for y in range(height):
                pygame.draw.line(colormap, self.coords_to_color(x,y), (x,y),(x,y))
        return colormap

class SatSliderButton(Button):

    def __init__(self, color_picker_overlay):
        self.rect = pygame.Rect((0,0),(20,480))
        self.parent = color_picker_overlay

    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            self.parent.user.active_color = self.coords_to_color(mouse_y)

    def coords_to_color(self, y):
        r,g,b = [i/255 for i in self.parent.user.active_color]
        h,l,s = colorsys.rgb_to_hls(r,g,b)
        width,height = self.rect.size
        color = colorsys.hls_to_rgb(h,l,float(y)/height)
        color = [i*255 for i in color]
        return color

    def draw(self):
        width, height = self.rect.size
        colormap = pygame.Surface(self.rect.size)

        for y in range(height):
            pygame.draw.line(colormap, self.coords_to_color(y), (0,y),(width,y))
        return colormap

class ActiveColorButton(Button):

    def __init__(self, color_picker_overlay):
        self.rect = pygame.Rect((0,0),(64,64))
        self.texture = pygame.Surface((64,64))
        self.parent = color_picker_overlay

    def left_click(self, mouse_x, mouse_y):
        pass

    def draw(self):
        self.texture.fill(self.parent.user.active_color)
        return self.texture
