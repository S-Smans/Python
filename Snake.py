import pygame

pygame.init()

display_width = 500
display_height = 500

black = (0, 0, 0)
dark_green = (0, 100, 0)
green = (0, 255, 0)
red = (255, 0, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")


def snake():
    pygame.draw.rect(game_display, dark_green, [int(display_width / 2), int(display_height / 2), 25, 25])


game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
    game_display.fill(black)
    snake()
    pygame.display.update()
pygame.quit()
quit()
