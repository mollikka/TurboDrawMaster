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

    def right_click(self, mouse_x, mouse_y):

        for button,location in self.buttons:
            bx,by = location
            x,y = mouse_x - bx, mouse_y - by
            button.right_click(x,y)

class Button(object):

    def __init__(self, parent):
        self.rect = pygame.Rect((0,0),(0,0))
        self.texture = pygame.Surface((0,0))
        self.parent = parent

    def draw(self):
        return self.texture

    def left_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            print "CLICK!"

    def right_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint((mouse_x,mouse_y)):
            print "CLICK!"

