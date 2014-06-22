import pygame

class Overlay(object):

    def __init__(self):
        self.name = "Overlay"

    def draw(self, window_size):

        surf = pygame.Surface(window_size)
        surf.fill((128,0,0))
        return surf
