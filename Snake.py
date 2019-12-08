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
    pygame.draw.rect(game_display, dark_green, [lead_x, lead_y, 25, 25])


game_exit = False

lead_x = 250
lead_y = 250
lead_new_x = 0
lead_new_y = 0

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_new_y = 0
                lead_new_x = - 25
            if event.key == pygame.K_RIGHT:
                lead_new_y = 0
                lead_new_x = + 25
            if event.key == pygame.K_DOWN:
                lead_new_x = 0
                lead_new_y = + 25
            if event.key == pygame.K_UP:
                lead_new_x = 0
                lead_new_y = - 25

    lead_y += lead_new_y
    lead_x += lead_new_x
    game_display.fill(black)
    snake()
    pygame.display.update()
    pygame.time.delay(60)

pygame.quit()
quit()

