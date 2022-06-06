class Directionals:
    def __init__(self):
        # directionals
        # Left
        self.moving_left = []  # images
        self.n_left = 0  # start sprite
        self.time_to_move_left = 11  # count to move left smootly
        # Right
        self.moving_right = []  # images
        self.n_right = 0  # start sprite
        self.time_to_move_right = 11  # count to move right smootly
        # Up
        self.moving_top = []  # images
        self.n_top = 0  # start sprite
        self.time_to_move_top = 11  # count to move up smootly
        # Down
        self.moving_down = []  # images
        self.n_down = 0  # start sprite
        self.time_to_move_down = 11  # count to move down smootly