import pygame

class Tool(object):

    def __init__(self):
        pass

    def draw(self, layer, mouse_location, ctrl, shift, alt):
        x,y = mouse_location
        pygame.draw.line(layer.surface, (255,255,255), (x,y), (x,y), 1)
