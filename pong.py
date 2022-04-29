import pygame

width = 500
height = 400
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Game Variables
exit_game = False
game_over = False

# Ball Variables
ball_x = 50
ball_y = 50
ball_vel_x = 0.1
ball_vel_y = 0.1

# Reflector Variables
reflector_x = 250
reflector_y = 370
reflector_vel_x = 70

while not exit_game:

    while not game_over:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit_game = True
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RIGHT):
                    reflector_x += reflector_vel_x
                if(event.key == pygame.K_LEFT):
                    reflector_x -= reflector_vel_x

        # >>>>> Ball Motion
        ball_x += ball_vel_x
        ball_y += ball_vel_y
        
        # boundary_check
        if(ball_y >= width):
            game_over = True
        elif(ball_x <= 0 or ball_x >= width):
            ball_vel_x = -ball_vel_x
        elif (ball_y <= 0):
            ball_vel_y = -ball_vel_y
        elif(ball_x <= (reflector_x + 100) and ball_x >= reflector_x and ball_y >= reflector_y ):
            ball_vel_y = -ball_vel_y

        # Display
        game_window.fill((255, 255, 255))
        pygame.draw.circle(game_window, (0, 0, 0), (ball_x, ball_y), 10, 10)
        pygame.draw.rect(game_window, (0, 0, 0), [
                        reflector_x, reflector_y, 100, 5])

        pygame.display.update()
    game_over()
