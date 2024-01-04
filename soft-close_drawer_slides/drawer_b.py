"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

from drawerlab.mass_spring_damper import MassSpringDamperODE
from drawerlab.drawer import Drawer

import matplotlib.pyplot as plt 
from drawerlab.settings import Settings
from drawerlab.make_video import Video

import sys
import os
import pygame


def plot_figures(t, position, velocity, show_plots = False):
    plt.figure('Position vs Time')    
    plt.plot(t, position); plt.ylabel('position (m)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-b2i.png')
    if show_plots:
        plt.show()

    plt.figure('Velocity vs Time')
    plt.plot(t, velocity); plt.ylabel('velocity (m/s)'); plt.xlabel('time (sec)'); plt.grid(); 
    plt.savefig('drawer-b2ii.png')
    if show_plots:
        plt.show() 



class DrawerAnimation:
    """Animating a drawer"""

    def __init__(self, tf, N):
        """Initialize the GUI and resources"""
        pygame.init()
        self.settings = Settings()
        self.N = N
        self.delta_t = tf/N          # delta t, e.g. 0.01 sec. N is number of point of simulation, and tf is simulation duration

        self.show_animation = self.settings.show_animation

        if self.show_animation:
            # Set the background color
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            pygame.display.set_caption('Drawer Simulation')
            self.bg_color = self.settings.bg_color
            self.text_font = pygame.font.SysFont(self.settings.font_name, self.settings.font_size)
            self.font_color = self.settings.font_color 
            self.text_location = self.settings.text_location
            self.make_video = self.settings.make_video

            # animation object
            self.drawer_animation = Drawer(self)
            if self.make_video == True: self.video = Video(os.getcwd())

    def run_animation(self, position, velocity):
        """Start the main loop for simulation"""
        i = 0
        closer_time = 0

        # simulation is for 10,000 miliseconds (1000*self.tf). 
        # we will run the results every 10 miliseconds.
        delay_time = int(1000*self.delta_t) 
        while True:
            self._check_events()
            slider_location_pixel = self.drawer_animation.slider_location(position[i])
            self._update_screen(slider_location_pixel, closer_time)


            pygame.time.delay(delay_time)

            #if slider_location_pixel < self.drawer_animation.drawer_middle and i < 990:
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

    def _update_screen(self, position, closer_time):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)     

        self.drawer_animation.draw_frame()
        self.drawer_animation.draw_slider(position)
  
        time_img = self.text_font.render(str(closer_time) + " ms", True, self.font_color)    
        self.screen.blit(time_img, self.text_location)
        pygame.display.update()

        # Make the most recently drawn screen visible
        pygame.display.flip()


def main():
    msd = MassSpringDamperODE(m = 1, c = 2, k = 3, x0 = 0.5, v0 = 0, tf= 10, N = 1000)
    t, position, velocity, number_of_points = msd.solve_motion()
    plot_figures(t, position, velocity)

    sim = DrawerAnimation(tf = 10, N = 1000)
    if sim.show_animation:
        sim.run_animation(position, velocity)    

if __name__ == '__main__':
    main()
