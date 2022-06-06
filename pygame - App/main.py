import pygame
from Display_Measurements import Display_Measurements
from Player import Player
from Close_Game_Function import close_game_function
from key_pressed_conditions import key_pressed_conditions
from Power_Up import Power_Up
from Make_Power_Ups import make_power_ups
from Wall import Wall
from Display_Arrays import display_array_for_categorys, display_array_for_power_ups

from Assign_Instances_To_Array import assign_instances_to_array

class Application(Display_Measurements):
    def __init__(self):
        #set_display_measurements
        Display_Measurements.__init__(self)

        #Player
        self.player = None

        #Screen
        self.gameDisplay = None

        #App Fps clock
        self.clock = pygame.time.Clock()

        #Walls
        self.category_object_container = []

    def set_walls(self, container):
        array_holder = []
        for element in container:
            array_holder.append(element)
        self.category_object_container.append(array_holder)
    def run(self):
        pygame.init()
        pygame.font.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))

        while True:
            close_game_function(pygame)  #Close the game fuction

            self.gameDisplay.fill((0,0,0))
            self.gameDisplay.blit(self.player.img, (self.player.x, self.player.y))
            #
            display_array_for_power_ups(self.gameDisplay, self.player.power_ups)
            #Si la ara;a coje el mushroom
            #Display text box in the middle of the screen
            key_pressed = pygame.key.get_pressed()
            key_pressed_conditions(key_pressed, pygame, self.player)
            self.player.power_up_effect(self.gameDisplay)
            #
            display_array_for_categorys(self.gameDisplay, self.category_object_container)
            self.clock.tick(30)
            #print(self.player.x, self.player.y)
            pygame.display.update()


def main():

    a = Application()
    # creame una aplicacion de 500 width y 500 height.
    display_x,display_y = 1000,800
    a.set_display_measurements(display_x, display_y)

    #Que tenga un jugador tipo Spider
    spider = Player()
    #Apariencia del jugador
    spider.appearance('spider.png')


    a.player = spider
    a.player.set_position(200,200) #player position

                            #Images for moving
                            # left, right, top, down
    a.player.set_imgs_moving(["Movement/Left/1.png","Movement/Left/2.png","Movement/Left/3.png"],
                             ["Movement/Right/1.png","Movement/Right/2.png","Movement/Right/3.png"],
                             ["Movement/Top/1.png","Movement/Top/2.png","Movement/Top/3.png"],
                             ["Movement/Down/1.png","Movement/Down/2.png","Movement/Down/3.png"])


    #defining Power Ups
    #make_power_ups(blue, "Blue")
    blue = Power_Up()
    make_power_ups(blue,"blue mushroom", "blue",(740,200))

    yellow = Power_Up()
    make_power_ups(yellow,"yellow mushroom", "yellow",(740,450))

    red = Power_Up()
    make_power_ups(red,"red mushroom", "red",(740,640))

    # Create walls
    walls = []
    x,y = 0,0
    counter = 0

    counter = assign_instances_to_array(Wall,walls,x,y,counter, 100,increment_x=True)
    counter = assign_instances_to_array(Wall, walls, x, y, counter, 100, increment_y=True)
    y = display_y - 100
    counter = assign_instances_to_array(Wall, walls, x, y, counter, 100,increment_x=True)
    y=0
    x = display_x - 100
    counter = assign_instances_to_array(Wall, walls, x, y, counter, 100, increment_y=True)



    #Assigning to application

    #Power Ups
    a.player.set_power_up(blue)
    a.player.set_power_up(yellow)
    a.player.set_power_up(red)

    #Walls
    a.set_walls(walls)

    #Pon la applicacion a correr
    a.run()



if __name__=='__main__':
    main()