import pygame

class Appearance:
    def __init__(self):
        self.img = None

    def appearance(self, img):
        self.img = pygame.image.load(img)