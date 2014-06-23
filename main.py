import sys

try:
    import pygame
except ImportError:
    print "Couldn't find a Pygame installation"

from manager import Manager

class System(object):

    def __init__(self):

        self.manager = Manager()

    def step(self):

        self.manager.handle_input()

        self.manager.draw()

def main():

    pygame.init()
    v = System()
    while True: v.step()

if __name__ == '__main__':
    sys.exit(main())
