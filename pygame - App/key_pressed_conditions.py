def key_pressed_conditions(key_pressed,pygame,player):
    if key_pressed[pygame.K_a] or key_pressed[pygame.K_d] or key_pressed[pygame.K_w] or key_pressed[pygame.K_s]:
        if key_pressed[pygame.K_a]:
            player.move_left()
        if key_pressed[pygame.K_d]:
            player.move_right()
        if key_pressed[pygame.K_w]:
            player.move_top()
        if key_pressed[pygame.K_s]:
            player.move_down()