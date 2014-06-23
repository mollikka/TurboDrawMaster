import pygame

class Overlay(object):

    def __init__(self, user):
        self.name = "Overlay"
        self.text = pygame.font.SysFont(None,48)
        self.buttons = [] #[[button, location], ..]
        self.user = user

    def draw(self, window_size):

        surf = pygame.Surface(window_size)
        surf.fill((32,32,32))
        surf.blit(self.text.render(self.name, True, (255,255,255)),(0,0))

        for button,location in self.buttons:
            surf.blit(button.draw(),location)

        return surf

    def left_click(self, mouse_x, mouse_y):

        for button,location in self.buttons:
            bx,by = location
            x,y = mouse_x - bx, mouse_y - by
            button.left_click(x,y)

import colorsys

class ColorPickerOverlay(Overlay):

    def __init__(self, user):
        super(ColorPickerOverlay,self).__init__(user)
        self.name = "Color Picker"

        self.buttons.append([ColorButton(self),(100,100)])
        self.buttons.append([ActiveColorButton(self),(0,100)])

class Button(object):

    def __init__(self, parent):
        self.rect = pygame.Rect((0,0),(0,0))
        self.texture = pygame.Surface((0,0))
        self.parent = parent

    def draw(self):
        return self.texture

    def left_click(self, mouse_x, mouse_y):
        if self.rect.hit((mouse_x,mouse_y)):
            print "CLICK!"

class ColorButton(Button):

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
