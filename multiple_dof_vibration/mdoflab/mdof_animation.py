import pygame
import sys
import math
import numpy as np
from mdoflab.mdof_animation_settings import Settings
from mdoflab.make_video import Video
import os


class MDOFAnimation():
    """A class for MDOF animation"""

    def __init__(self, m, k, x0, v0, tf = 40, N = 4000):
        
        self.m = m              # mass
        self.k = k              # spring constant
        self.x0 = x0            # initial position
        self.v0 = v0            # initial velocity  
        self.tf = tf            # sim time
        self.N = N              # number of steps

        pygame.init()
        self.settings = Settings()

        self.show_animation = self.settings.show_animation

        if self.show_animation:
            self.screen_height = self.settings.screen_height
            if self.k[0] == 0: 
                self.screen_width = self.settings.screen_width
            else:    
                self.screen_width = self.settings.screen_width/2

            # Set the background color
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
            pygame.display.set_caption('MDOF Mass-Spring Simulation')
            self.bg_color = self.settings.bg_color
            self.text_font = pygame.font.SysFont(self.settings.font_name, self.settings.font_size)
            self.font_color = self.settings.font_color 
            self.text_location = self.settings.text_location

            self.screen_rect = self.screen.get_rect()    



            self.mass_position = self.settings.mass_position
            self.mass_length = self.settings.mass_length
            self.mass_height = self.settings.mass_height
            self.spring_position = self.settings.spring_position
            self.spring_length = self.settings.spring_length
            self.spring_height = self.settings.spring_height  

            self.font_color = self.settings.font_color    
            self.text_font = pygame.font.SysFont(self.settings.font_name, self.settings.font_size)
            self.text_location = self.settings.text_location    


            self.red = self.settings.red
            self.green = self.settings.green
            self.blue = self.settings.blue
            self.black = self.settings.black
            self.white = self.settings.white
            self.cyan = self.settings.cyan

            self.colors = [self.red, self.green, self.blue, self.black, self.cyan]

            self.make_video = self.settings.make_video

            # animation object
            #self.drawer_animation = Drawer(self)
            if self.make_video == True: self.video = Video(os.getcwd())

    def draw_text(self):
        """Write the values of mass and springs"""
        mass_img = self.text_font.render("m1 = " + str(self.m[0]) + " kg,   " + \
                                         "m2 = " + str(self.m[1]) + " kg,   " + \
                                         "m3 = " + str(self.m[2]) + " kg    " \
                                          , True, self.font_color)    
        self.screen.blit(mass_img, self.text_location)

        if self.k[0] is 0:
            spring_img = self.text_font.render("k2 = " + str(self.k[1]) + " N/m,   " + \
                                             "k3 = " + str(self.k[2]) + " N/m,   " \
                                             , True, self.font_color)    
        else:    
            spring_img = self.text_font.render("k1 = " + str(self.k[0]) + " N/m,   " + \
                                             "k2 = " + str(self.k[1]) + " N/m,   " + \
                                             "k3 = " + str(self.k[2]) + " N/m,   " + \
                                             "k4 = " + str(self.k[3]) + " N/m,   " \
                                              , True, self.font_color)    

        self.screen.blit(spring_img, (self.text_location[0], self.text_location[1]+30))

        x0_img = self.text_font.render("x1(0) = " + str(self.x0[0]) + " m,   " + \
                                         "x2(0) = " + str(self.x0[1]) + " m,   " + \
                                         "x3(0) = " + str(self.x0[2]) + " m    " \
                                          , True, self.font_color)    
        self.screen.blit(x0_img, (self.text_location[0], self.text_location[1]+60))

        v0_img = self.text_font.render("v1(0) = " + str(self.v0[0]) + " m/s,   " + \
                                         "v2(0) = " + str(self.v0[1]) + " m/s,   " + \
                                         "v3(0) = " + str(self.v0[2]) + " m/s    " \
                                          , True, self.font_color)    
        self.screen.blit(v0_img, (self.text_location[0], self.text_location[1]+90))

        pygame.display.update()    


    def draw_floor(self):
        """Draw the floor and wall"""

        wall_color = (10,10,10)

        y = (self.screen_height - 100) + 2

        # floor
        pygame.draw.line(self.screen, wall_color,\
            [5, y + self.mass_height/2],\
            [self.screen_width-1, y + self.mass_height/2],\
            5)   


        # wall1
        pygame.draw.line(self.screen, wall_color,\
            [5, 0],\
            [5, y + self.mass_height/2],\
            5)   


        # wall2
        pygame.draw.line(self.screen, wall_color,\
            [-5+self.screen_width, 0],\
            [-5+self.screen_width, y + self.mass_height/2],\
            5)   


    def draw_mass(self, pos):
        """Draw mass"""

        door_color = (150,150,150)
        slider_color = (10,10,10)

        y = (self.screen_height - 100 )

        if self.k[0] == 0:
            gap = self.screen_width/8    
        else:
            gap = self.screen_width/4

        # draw springs
        for mi in range(0,4):
            if self.k[mi] is not 0:
                spring_img = self.text_font.render("k"+str(mi+1) , True, self.font_color) 

                if mi is 0:
                    start_x = 5 
                    stop_x  = gap + mi*gap   + pos[mi]
                elif mi == 3:
                    start_x  = gap + (mi-1)*gap   + pos[mi-1]                    
                    stop_x  = gap*4 - 5                   
                else:
                    start_x  = gap + (mi-1)*gap   + pos[mi-1]                    
                    stop_x  = gap + mi*gap   + pos[mi]                    
                  
                start_y = y
                stop_y = y

                thickness = 10
                pygame.draw.line(self.screen, self.black, \
                    [start_x, start_y], \
                    [stop_x,  stop_y ], \
                    thickness)

                mid_x = (start_x+stop_x)/2 - 20
                mid_y = (start_y+stop_y)/2 - 25

                self.screen.blit(spring_img, (mid_x, mid_y))


        # draw masses (with text)
        for mi in range(0,3):
            bias = gap + mi*gap 
            pygame.draw.rect(self.screen, self.colors[mi], \
                pygame.Rect(bias+pos[mi] - self.mass_length/2, y - self.mass_height/2, self.mass_length, self.mass_height),\
                0)

            mass_img = self.text_font.render("m"+str(mi+1) , True, self.font_color)    
            self.screen.blit(mass_img, (bias+pos[mi] - self.mass_length/4, y - self.mass_height/4))


    def draw_start(self, pos):
        """Draw mass"""

        door_color = (150,150,150)
        slider_color = (10,10,10)


        # draw springs
        start_img = self.text_font.render("Start" , True, self.font_color) 
        self.screen.blit(spring_img, (300, 800))

        pygame.draw.rect(self.screen, self.green, \
        pygame.Rect(300, 800, 100, 50),\
        0)


    def run_animation(self, X):
        """Start the main loop for simulation"""
        i = 0
        closer_time = 0

        # simulation is for 10,000 miliseconds (1000*self.tf). 
        # we will run the results every 10 miliseconds.
        delay_time = int(10*self.tf/self.N) 
        while True:
            self._check_events()
            self._update_screen(100*X[:,i], closer_time)
            pygame.time.delay(delay_time)
            #if  i < self.N - 1:    
            #    i += 1
            #    closer_time += delay_time   

            if  i < self.N - 1:    
                i += 1
                closer_time += delay_time
                if self.make_video == True: self.video.make_png(self.screen)
            else: 
                if self.make_video == True: self.video.make_mp4()
                break


    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self, pos, closer_time):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)     

        
        self.draw_floor()
        self.draw_mass(pos)
        self.draw_text()
  
        #time_img = self.text_font.render(str(closer_time) + " ms", True, self.font_color)    
        #self.screen.blit(time_img, self.text_location)
        pygame.display.update()

        # Make the most recently drawn screen visible
        pygame.display.flip()                
