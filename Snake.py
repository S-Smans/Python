import pygame
import random

pygame.init()

display_width = 500
display_height = 500
snake_size = 25
FPS = 17

black = (0, 0, 0)
dark_green = (0, 100, 0)
green = (0, 255, 0)
red = (255, 0, 0)


game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [int(display_height / 2), int(display_width / 2)])


def snake(lead_x, lead_y):
    pygame.draw.rect(game_display, dark_green, [lead_x, lead_y, snake_size, snake_size])


def food(rand_x, rand_y):
    pygame.draw.rect(game_display, red, [rand_x, rand_y, snake_size, snake_size])


clock = pygame.time.Clock()


def game_loop():
    game_exit = False
    game_over = False

    rand_x = random.randrange(0, display_width - snake_size, snake_size)
    rand_y = random.randrange(0, display_height - snake_size, snake_size)

    lead_x = int(display_width / 2)
    lead_y = int(display_height / 2)

    lead_new_x = 0
    lead_new_y = 0
    while not game_exit:

        while game_over:
            game_display.fill(black)
            message_to_screen("game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_new_y = 0
                    lead_new_x = - snake_size
                elif event.key == pygame.K_RIGHT:
                    lead_new_y = 0
                    lead_new_x = + snake_size
                elif event.key == pygame.K_DOWN:
                    lead_new_x = 0
                    lead_new_y = + snake_size
                elif event.key == pygame.K_UP:
                    lead_new_x = 0
                    lead_new_y = - snake_size
        if lead_x >= display_width:
            lead_x = 0
        elif lead_x < 0:
            lead_x = display_width
        elif lead_y >= display_height:
            lead_y = 0
        elif lead_y < 0:
            lead_y = display_height

        lead_y += lead_new_y
        lead_x += lead_new_x

        game_display.fill(black)

        food(rand_x, rand_y)
        snake(lead_x, lead_y)

        pygame.display.update()

        if lead_x == rand_x and lead_y == rand_y:
            print("nom")

        clock.tick(FPS)

    pygame.quit()
    quit()


game_loop()
