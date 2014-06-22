import pygame

from manager import Manager

class System(object):

    def __init__(self):

        self.manager = Manager()

    def step(self):

        for event in pygame.event.get():
            self.manager.handle(event)

        self.manager.draw()
