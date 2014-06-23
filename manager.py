import sys
import pygame

import overlays
from picture import Picture
from user_state import User

class Manager(object):

    def __init__(self):

        self.background_color = (0,0,0)
        self.resize_window((800,600))
        self.picture = Picture()

        self.user = User()

        self.active_overlay = None
        self.test_overlay = overlays.Overlay(self.user)
        self.color_picker_overlay = overlays.ColorPickerOverlay(self.user)

    def get_active_color(self):
        return self.user.active_color

    def get_active_tool(self):
        return self.user.active_tool

    def resize_window(self, size):

        self.window=pygame.display.set_mode(size,pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)
        self.window.fill(self.background_color)
        pygame.display.flip()

    def draw(self):

        #clear the screen
        self.window.fill(self.background_color)

        #draw the picture
        if self.picture:
            pic_surf = self.picture.draw()

            disp_pic_surf = self.apply_camera_to_picture(pic_surf)
            self.window.blit(disp_pic_surf, (0,0))

        #draw the active overlay
        if self.active_overlay:
            ovr_surf = self.active_overlay.draw(self.window.get_size())
            self.window.blit(ovr_surf, (0,0))

        #update the screen
        pygame.display.flip()

    def apply_camera_to_picture(self, pic_surf):

        return pic_surf

    def handle_input(self):

        #mouse.get_rel must only be called once a step, don't call elsewhere
        #(because it's relative to the last call)
        mouse_delta = pygame.mouse.get_rel()
        mouse_pos = pygame.mouse.get_pos()

        mouse_pressed = pygame.mouse.get_pressed()
        mouse_left_pressed, mouse_mid_pressed, mouse_right_pressed = mouse_pressed

        mod_pressed = pygame.key.get_mods()
        shift_pressed = mod_pressed & pygame.KMOD_SHIFT
        ctrl_pressed = mod_pressed & pygame.KMOD_CTRL
        alt_pressed = mod_pressed & pygame.KMOD_ALT

        self.active_overlay = None

        if ctrl_pressed:
            self.active_overlay = self.test_overlay
        if pygame.key.get_pressed()[pygame.K_q]:
            self.active_overlay = self.color_picker_overlay

        if self.active_overlay:
            if mouse_left_pressed:
                mx,my = mouse_pos
                self.active_overlay.left_click(mx,my)
        else:
            #drawing mode
            if mouse_left_pressed:
                layer = self.picture.layers[0]
                color = self.get_active_color()
                self.get_active_tool().draw(layer, color, pygame.mouse.get_pos(), 
                            ctrl_pressed, shift_pressed, alt_pressed)

        for event in pygame.event.get():
            #SYSTEM EVENTS
            if event.type == pygame.QUIT:
                sys.exit(0)

            elif event.type == pygame.VIDEORESIZE:
                self.resize_window(event.dict['size'])
