from Movement import Movement
import pygame
class Player(Movement):
    def __init__(self):
        self.name = None
        self.inventory = []

        #Player movements + appearance
        Movement.__init__(self)

        self.power_ups = []

    def set_power_up(self,power_up):
        self.power_ups.append(power_up)

    def power_up_effect(self,gameDisplay):
        for power_up in self.power_ups:
            condition_1 = self.x >= power_up.x - 70 and self.x <= power_up.x + 70
            condition_2 = self.y >= power_up.y - 70 and self.y <= power_up.y + 70
            condition_3 = power_up in self.inventory
            if (condition_1 and condition_2) and not condition_3:
                power_up.inventory_store_time+= 1
                if power_up.inventory_store_time > 100:
                    self.inventory.append(power_up)
                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                text_surface = my_font.render(f'You obtained the {power_up.name}', False, (255, 255, 255))

                gameDisplay.blit(text_surface, (400, 400))  # positions are intended to changedddd
                self.imgs_moving_left = power_up.power_up_imgs_moving_left
                self.imgs_moving_right = power_up.power_up_imgs_moving_right
                self.imgs_moving_top = power_up.power_up_imgs_moving_top
                self.imgs_moving_down = power_up.power_up_imgs_moving_down

            else:
                power_up.inventory_store_time = 0

