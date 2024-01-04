"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

import pygame
import math
import numpy as np
from drawerlab.settings import Settings

class Drawer():
    """A class for various door parts"""

    def __init__(self, sim):
        """Initiate the robot and set its start position"""
        self.screen = sim.screen
        self.screen_rect = sim.screen.get_rect()    

        self.settings = Settings()
        #self.drawer_middle = self.settings.drawer_middle 
        self.left_frame_pos = self.settings.left_frame_pos 
        self.middle_frame_pos = self.settings.middle_frame_pos 
        self.frame_thicnkess = self.settings.frame_thicnkess 
        self.frame_width = self.settings.frame_width
        self.frame_height = self.settings.frame_height

    def draw_frame(self):
        """Draw the drawer frame"""

        frame_color = (100,10,0)

        pygame.draw.rect(self.screen, frame_color, \
            pygame.Rect(self.middle_frame_pos+self.left_frame_pos-self.frame_thicnkess, 80, \
                self.frame_width, self.frame_height),  self.frame_thicnkess)


    def draw_slider(self, open_position):
        """Draw the drawer"""

        drawer_color = (150,150,0)

        # drawer frame
        pygame.draw.rect(self.screen, drawer_color, pygame.Rect(self.left_frame_pos - 10 + self.frame_thicnkess+open_position, \
            80 + self.frame_thicnkess, \
            self.frame_width - 2*self.frame_thicnkess, self.frame_height - 2*self.frame_thicnkess),\
              self.frame_thicnkess)
        
        # drawe handle
        pygame.draw.line(self.screen, drawer_color, [open_position+30, 210], [open_position+30, 260], 20)      
        

    def slider_location(self, position):
        """Gets the position of door in meters and returns the location in pixels""" 
        return self.left_frame_pos + self.middle_frame_pos - 4*self.frame_thicnkess -np.round(150*position)   
