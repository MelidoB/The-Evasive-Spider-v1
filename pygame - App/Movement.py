from Setting_Images import Setting_Images
from Setting_Position import Setting_Position
from Directionals import Directionals
import pygame

class Movement(Setting_Position,Setting_Images,Directionals):
    def __init__(self):
        #coordinates
        Setting_Position.__init__(self)

        #images
        Setting_Images.__init__(self)

        #Directionals
        Directionals.__init__(self)

    #setting_movement_fuctions
    def change_image(self, left = False, right = False, top = False):
        if left:
            if self.n_left >= len(self.imgs_moving_left) - 1:
                self.n_left = 0
            else:
                self.n_left += 1

            if self.time_to_move_left > 4:
                self.img = self.imgs_moving_left[self.n_left]
                self.time_to_move_left = 0

            self.time_to_move_left += 1
        elif right:
            if self.n_right >= len(self.imgs_moving_right) - 1:
                self.n_right = 0
            else:
                self.n_right += 1

            if self.time_to_move_right > 4:
                self.img = self.imgs_moving_right[self.n_right]
                self.time_to_move_right = 0

            self.time_to_move_right += 1
        elif top:
            if self.n_top >= len(self.imgs_moving_top) - 1:
                self.n_top = 0
            else:
                self.n_top += 1

            if self.time_to_move_top > 4:
                self.img = self.imgs_moving_top[self.n_top]
                self.time_to_move_top = 0

            self.time_to_move_top += 1
        else:
            if self.n_down >= len(self.imgs_moving_down) - 1:
                self.n_down = 0
            else:
                self.n_down += 1

            if self.time_to_move_down > 4:
                self.img = self.imgs_moving_down[self.n_down]
                self.time_to_move_down = 0

            self.time_to_move_down += 1

    def move_left(self):
        #can't move left if there's an object at the left
        #If object.x
        self.x -= 10
        self.change_image(left=True)
    def move_right(self):
        self.x += 10
        self.change_image(right=True)
    def move_top(self):
        self.y -= 10
        self.change_image(top=True)
    def move_down(self):
        self.y += 10
        self.change_image()