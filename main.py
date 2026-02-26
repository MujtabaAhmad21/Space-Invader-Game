import pygame
import random
import math

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png').convert_alpha()
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load('player.png').convert_alpha()
# cords of player appearing at start of game
player_x = 370
player_y = 480
player_x_change = 0

# enemy
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png').convert_alpha())
    enemy_x.append(random.randint(0, 800))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(5)
    enemy_y_change.append(40)

# bullet
# ready = you can't see the bullet on screen
# fire = the bullet is currently moving
bullet_image = pygame.image.load('bullet.png').convert_alpha()
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 7
bullet_state = 'ready'

background_image = pygame.image.load('background.png').convert()
def background():
    screen.blit(background_image, (0, 0))

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x+16, y+10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemy_x[i] - bullet_x, 2)) + (math.pow(enemy_y[i] - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False

clock = pygame.time.Clock()

# score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

score_x = 10
score_y = 10

def display_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

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
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # checking for boundries

    # player movement
    player_x += player_x_change

    if player_x < 0:
        player_x = 0
    elif player_x > 736:
        player_x = 736

    # enemy movement
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]

        if enemy_x[i] <= 0:
            enemy_x_change[i] = 5
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -5
            enemy_y[i] += enemy_y_change[i]

        # collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemy_x[i] = random.randint(0, 800)
            enemy_y[i] = random.randint(50, 150)
        
        enemy(enemy_x[i], enemy_y[i], i)

    
    # bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    player(player_x, player_y)
    display_score(score_x, score_y)
    pygame.display.update()
    clock.tick(60)