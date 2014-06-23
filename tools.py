import pygame

class Tool(object):

    def __init__(self):
        pass

    def draw(self, layer, color, mouse_location, ctrl, shift, alt):
        x,y = mouse_location
        pygame.draw.line(layer.surface, color, (x,y), (x,y), 1)
