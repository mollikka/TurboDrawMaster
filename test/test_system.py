import unittest
import pygame
import main

class TestSystemManager(unittest.TestCase):

    def test_system(self):
        pygame.init()
        self.v = main.System()
        self.v.step()
