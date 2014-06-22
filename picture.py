import pygame

class Picture(object):

    def __init__(self):
        self.new_image(800,600)

    def new_image(self, width, height):
        self.layers = [Layer(width,height)]
        self.size = width, height

    def draw(self):
        surface = pygame.Surface((self.size),pygame.SRCALPHA)
        for layer in self.layers:
            layer.draw(surface)
        return surface

class Layer(object):

    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height),pygame.SRCALPHA)
        self.surface.fill(0)

    def draw(self, surface):
        surface.blit(self.surface, (0,0))

