import pygame
import random
pygame.init()
display_height = 500
display_width = 500
game_display = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Snake")
background_color = (0, 0, 0)
clock = pygame.time.Clock()
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

block_size = 20


def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(game_display, snake_color, [XnY[0], XnY[1], block_size, block_size])


def game_loop():
    random_food_x = random.randrange(0, 260, 20)
    random_food_y = random.randrange(0, 260, 20)
    xy_food = random_food_x, random_food_y
    crashed = False
    vertical_change = 0
    horizontal_change = 0
    x_snake_new = 260
    y_snake_new = 260
    snake_list = []
    snake_length = 1
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    horizontal_change = 0
                    vertical_change += 20

                    if vertical_change == 40:
                        vertical_change = 20

                if event.key == pygame.K_UP:
                    horizontal_change = 0
                    vertical_change -= 20

                    if vertical_change == -40:
                        vertical_change = -20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    vertical_change = 0
                    horizontal_change -= 20

                    if horizontal_change == -40:
                        horizontal_change = -20

                if event.key == pygame.K_RIGHT:
                    vertical_change = 0
                    horizontal_change += 20
                    if horizontal_change == 40:
                        horizontal_change = 20
        y_snake_new += vertical_change
        x_snake_new += horizontal_change
        xy_snake = x_snake_new, y_snake_new
        xy_food = random_food_x, random_food_y
        if xy_food == xy_snake:
            random_food_x = random.randrange(0, 260, 20)
            random_food_y = random.randrange(0, 260, 20)
            snake_length += 1
        game_display.fill(background_color)
        pygame.draw.rect(game_display, food_color, [random_food_x, random_food_y, 20, 20])
        snake_head = []
        snake_head.append(x_snake_new)
        snake_head.append(y_snake_new)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        print(snake_list)
        print(snake_length)
        snake(block_size, snake_list)
        pygame.display.update()
        clock.tick(10)
game_loop()
pygame.quit()
quit()
