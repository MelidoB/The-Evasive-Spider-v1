from Appearance import Appearance
from Image_Pygame_Format import image_pygame_format

class Setting_Images(Appearance):
    def __init__(self):
        Appearance.__init__(self)
        self.imgs_moving_left = []
        self.imgs_moving_right = []
        self.imgs_moving_top = []
        self.imgs_moving_down = []

    def set_image_objects(self,images_array, store_img):
        """convert imgs.png to pygame format"""
        for image in images_array:
            img = image_pygame_format(image)
            store_img.append(img)
    def set_imgs_moving(self, left, right, top, down):
        """ get's images.png and assigns it to player imgs moving"""
        self.set_image_objects(left,self.imgs_moving_left)
        self.set_image_objects(right,self.imgs_moving_right)
        self.set_image_objects(top,self.imgs_moving_top)
        self.set_image_objects(down,self.imgs_moving_down)