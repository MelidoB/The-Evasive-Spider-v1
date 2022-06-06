from Set_Power_Up_Imgs_Facilitator import set_power_up_imgs_facilitator

def make_power_ups(object,name, color,coord):
    object.set_name(name)
    coord_x,coord_y = coord
    object.appearance(f'{color}_mushroom.png')
    object.set_position(coord_x, coord_y)
    z, x, c, v = set_power_up_imgs_facilitator(
        color.capitalize())  # This changes the color to find to change the file location for that color
    object.set_power_up_imgs(z, x, c, v)