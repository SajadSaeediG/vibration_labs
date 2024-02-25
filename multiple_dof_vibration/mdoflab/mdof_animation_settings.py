class Settings:
    """A class to store all setting of the simulation"""

    def __init__(self):
        """Initialize the settings of the simulation"""

        self.show_animation = True

        # Screen settings
        self.screen_width = 1280            # screen width (in pixles)
        self.screen_height = 480            # screen height (in pixles)
        self.bg_color = (230, 230, 230)     # screen background color

        # Sliding door animation parameters 
        self.font_size = 24                 # text font size
        self.font_name = 'calibri'          # text font name
        self.font_color = (100,0,0)         # text color
        self.text_location = (50, 100)      # text location on the screen

        self.red = (255, 0, 0)              # red
        self.green = (0, 255, 0)            # green
        self.blue = (0, 0, 255)             # blue
        self.black = (0, 0, 0)              # blue
        self.white = (255, 255, 255)        # white
        self.cyan = (0, 255, 255)           # cyan

        # Sliding door visualization parameters (all values are in pixels)
        self.mass_position = 300            #
        self.mass_length = 70               # x-position of the left 
        self.mass_height = 50               # x-position of the middle
        self.spring_position = 300
        self.spring_length = 40             # frame thickness
        self.spring_height = 5              # door-frame width
        self.frame_height = 300             # door-frame height

        # make video from animation
        self.make_video = False