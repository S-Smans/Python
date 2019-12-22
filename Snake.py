import pygame
import random

pygame.init()
pygame.font.init()

# Games settings
display_width = 600
display_height = 600
snake_size = 25
apple_size = 25
FPS = 17

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
dark_green = (0, 100, 0)
black = (0, 0, 0)
# Map variable
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake!")
# Word Font
font = pygame.font.SysFont("Comic Sans MS", 30)


# Pause Message
def message(msg, color):
    pause_text = font.render(msg, True, color)
    game_display.blit(pause_text, [int(display_width / 2), int(display_height / 2)])


# Snake function
def snake(snake_tail):
    for XnY in snake_tail:
        pygame.draw.rect(game_display, dark_green, [XnY[0], XnY[1], snake_size, snake_size])


# Apple function
def apple(apple_direction_x, apple_direction_y):
    pygame.draw.rect(game_display, red, [apple_direction_x, apple_direction_y, apple_size, apple_size])


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
    game_pause = False
    game_crashed = False

    # Game Clock
    clock = pygame.time.Clock()

    direction = ""
    snake_tail = []
    snake_length = 1
    while True:

        # Paused Loop
        while game_pause:
            game_display.fill(black)
            message("Game Paused!", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_pause = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        # Running Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    new_snake_y = 0
                    new_snake_x = -25
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    new_snake_y = 0
                    new_snake_x = 25
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    new_snake_x = 0
                    new_snake_y = -25
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    new_snake_x = 0
                    new_snake_y = 25
                    direction = "down"
                elif event.key == pygame.K_p:
                    game_pause = True

        # Eating apple
        if apple_x <= snake_x < apple_x + apple_size:
            if apple_y <= snake_y < apple_y + apple_size:
                apple_x = random.randrange(0, display_width, snake_size)
                apple_y = random.randrange(0, display_height, snake_size)
                snake_length += 1
        elif snake_x <= apple_x < snake_x + snake_size:
            if snake_y <= apple_y < snake_y + snake_size:
                apple_x = random.randrange(0, display_width, snake_size)
                apple_y = random.randrange(0, display_height, snake_size)
                snake_length += 1
        # Assigning new snake XnY values
        snake_x += new_snake_x
        snake_y += new_snake_y

        # Snake goes threw walls
        if snake_x >= display_width:
            snake_x = 0
        elif snake_x < 0:
            snake_x = display_width - snake_size
        elif snake_y >= display_height:
            snake_y = 0
        elif snake_y < 0:
            snake_y = display_height - snake_size

        # Snake Length list
        snake_head = [snake_x, snake_y]
        snake_tail.append(snake_head)

        # Snake Death when touching tail
        for each_block in snake_tail[1:-1]:
            if each_block == snake_head:
                game_crashed = True

        # Deletes snake trail
        if len(snake_tail) > snake_length:
            del snake_tail[0]

        # Calls apple and snake function
        game_display.fill(black)
        apple(apple_x, apple_y)
        snake(snake_tail)
        pygame.display.update()
        clock.tick(FPS)

        # Game Crashed Loop
        while game_crashed:
            game_display.fill(black)
            message("C Continue Q Quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_crashed = False
                        game_loop()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


game_loop()
