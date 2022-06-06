def assign_instances_to_array(Class,
                              array,
                              x,y,
                              counter,
                              increment_amount,
                              increment_x=False,increment_y=False):
    #Object, Array, x,y,counter,increment
    for i in range(counter,counter+12):
        array.append(Class())
        array[i].set_name("Wall {i}")
        array[i].appearance("wall.png")
        array[i].set_position(x,y)
        if increment_x:
            x+=increment_amount
        if increment_y:
            y+=increment_amount
        counter+=1

    return counter