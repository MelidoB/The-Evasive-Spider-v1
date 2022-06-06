def display_array_for_power_ups(display, container):
        for element in container:
            display.blit(element.img, (element.x, element.y))

def display_array_for_categorys(display, category):
    for container in category:
        for element in container:
            display.blit(element.img, (element.x, element.y))