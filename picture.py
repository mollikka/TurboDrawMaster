import pygame

class View(object):

    def __init__(self, picture):
        self.picture = picture
        self.panning = [0,0]
        self.zoom = 1

    def set_panning_relative(self, delta):
        self.panning[0] += delta[0]
        self.panning[1] += delta[1]

    def position_screen_to_picture(self, position):
        p = list(position)
        p[0] -= self.panning[0]
        p[1] -= self.panning[1]
        return p

    def draw(self, window_size):
        surf = pygame.Surface(window_size, pygame.SRCALPHA)
        pic = self.picture.draw()

        surf.blit(pic,self.panning)
        return surf

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

