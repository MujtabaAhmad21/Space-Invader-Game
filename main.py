import pygame
import random

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

# enemy
enemy_image = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.3
enemy_y_change = 40

# bullet
# ready = you can't see the bullet on screen
# fire = the bullet is currently moving
bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 0.5
bullet_state = 'ready'

background_image = pygame.image.load('background.png')
def background():
    screen.blit(background_image, (0, 0))

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y):
    screen.blit(enemy_image, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x+16, y+10))

# game loop
running = True
while running:
    # rgb
    screen.fill((0, 0, 0))
    background()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is being pressed, check if it is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # checking for boundries
    player_x += player_x_change

    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736

    
    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'ready'
    # bullet movement
    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()