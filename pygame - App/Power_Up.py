from Image_Pygame_Format import image_pygame_format
from Object_Basic_Information import ObjectBasicInformation

class Power_Up(ObjectBasicInformation):
    def __init__(self):
        ObjectBasicInformation.__init__(self)
        self.inventory_store_time = 0

        self.power_up_imgs_moving_left = []
        self.power_up_imgs_moving_right = []
        self.power_up_imgs_moving_top = []
        self.power_up_imgs_moving_down = []
    #


    def set_power_up_imgs(self,left,right,top,down):
        for image in left:
            img = image_pygame_format(image)
            self.power_up_imgs_moving_left.append(img)
        for image in right:
            img = image_pygame_format(image)
            self.power_up_imgs_moving_right.append(img)
        for image in top:
            img = image_pygame_format(image)
            self.power_up_imgs_moving_top.append(img)
        for image in down:
            img = image_pygame_format(image)
            self.power_up_imgs_moving_down.append(img)