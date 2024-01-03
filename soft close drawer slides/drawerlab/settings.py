"""
Vibration Computer Lab
Sajad Saeedi - 2024
Toronto Metropolitan University
"""

class Settings:
    """A class to store animation settings of the simulation"""

    def __init__(self):

        self.show_animation = True

        # Screen settings
        self.screen_width = 640             # screen width (in pixles)
        self.screen_height = 480            # screen height (in pixles)
        self.bg_color = (230, 230, 230)     # screen background color

        # Sliding door animation parameters 
        self.font_size = 48                 # text font size
        self.font_name = 'calibri.ttc'      # text font name
        self.font_color = (100,0,0)         # text color
        self.text_location = (50, 410)      # text location on the screen

        # Sliding door visualization parameters (all values are in pixels)
        self.drawer_middle = 190              #
        self.left_frame_pos = 30            # x-position of the left 
        self.middle_frame_pos = 200         # x-position of the middle
        self.right_frame_pos = 190
        self.frame_thicnkess = 10           # frame thickness
        self.frame_width = 200              # door-frame width
        self.frame_height = 300             # door-frame height

        # make video from animation
        self.make_video = False
