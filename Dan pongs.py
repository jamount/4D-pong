import pygame
from paddle import *

pygame.init()

green = (31, 222, 83)
black = (0, 0, 0)
white = (255, 255, 255)

size = (1400, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("4D Pong")

paddleA = Paddle(white, 20, 200)
paddleA.rect.x = 50
paddleA.rect.y = 700

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 600
paddleB.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

run = True

clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleA.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleA.moveDown(5)

    screen.fill(black)
    pygame.draw.line(screen, green, [698, 0], [698, 1000], 5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
