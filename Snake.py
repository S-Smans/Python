import pygame
import random

pygame.init()
pygame.font.init()
# Games settings
display_width = 600
display_height = 400
snake_size = 25
FPS = 17

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
dark_green = (0, 100, 0)
# Map variable
game_display = pygame.display.set_mode((display_width, display_height))

# Word Font
font = pygame.font.SysFont("Comic Sans MS", 30)


# Pause Message
def pause_message(msg, color):
    pause_text = font.render(msg, True, color)
    game_display.blit(pause_text, [int(display_width / 2), int(display_height / 2)])


# Snake function
def snake(snake_tail):
    for XnY in snake_tail:
        pygame.draw.rect(game_display, dark_green, [XnY[0], XnY[1], snake_size, snake_size])


# Apple function
def apple(apple_direction_x, apple_direction_y):
    pygame.draw.rect(game_display, red, [apple_direction_x, apple_direction_y, snake_size, snake_size])


# Main game loop
def game_loop():
    # Game variables
    snake_x = int(display_width / 2)
    snake_y = int(display_height / 2)

    new_snake_x = 0
    new_snake_y = 0

    # Apple Starting location
    apple_x = random.randrange(0, display_width, snake_size)
    apple_y = random.randrange(0, display_height, snake_size)

    # Game State
    game_over = False
    game_pause = False

    # Game Clock
    clock = pygame.time.Clock()

    snake_tail = []
    snake_length = 1
    while not game_over:

        # Paused Loop
        while game_pause:
            pygame.display.set_mode((display_width, display_height))
            pause_message("Game Paused!", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_pause = False
                elif event.type == pygame.QUIT:
                    game_pause = False
                    game_over = True

        # Running Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_snake_y = 0
                    new_snake_x = -25
                elif event.key == pygame.K_RIGHT:
                    new_snake_y = 0
                    new_snake_x = 25
                elif event.key == pygame.K_UP:
                    new_snake_x = 0
                    new_snake_y = -25
                elif event.key == pygame.K_DOWN:
                    new_snake_x = 0
                    new_snake_y = 25
                elif event.key == pygame.K_p:
                    game_pause = True

        # Eating apple
        if snake_x == apple_x and snake_y == apple_y:
            apple_x = random.randrange(0, display_width, snake_size)
            apple_y = random.randrange(0, display_height, snake_size)
            snake_length += 1

        snake_x += new_snake_x
        snake_y += new_snake_y

        snake_head = [snake_x, snake_y]
        snake_tail.append(snake_head)
        for each_block in snake_tail[1:-1]:
            if each_block == snake_head:
                game_over = True
        if len(snake_tail) > snake_length:
            del snake_tail[0]

        pygame.display.set_mode((display_width, display_height))
        apple(apple_x, apple_y)
        snake(snake_tail)
        pygame.display.update()

        clock.tick(FPS)


game_loop()
