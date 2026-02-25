import pygame

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load('player.png')
# cords of player appearing at start of game
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_image, (x, y))

# game loop
running = True
while running:
    # rgb
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is being pressed, check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player(player_x, player_y)
    pygame.display.update()