from Image_Pygame_Format import image_pygame_format


class ObjectBasicInformation:
    def __init__(self):
        self.name = None
        self.img = None
        self.x = None
        self.y = None

    def set_name(self, name):
        self.name = name

    def appearance(self, image):
        self.img = image_pygame_format(image)

    def set_position(self,x = 200,y=400):
        self.x = x
        self.y = y