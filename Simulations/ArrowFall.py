import pygame
import time
import random
import sys

brown = (137, 63, 69)
black = (0, 0, 0)
white = (255, 255, 255)
green = (124, 252, 0)

screen = pygame.display.set_mode((800, 600))

arrow_size = (5, 25)
arrow = pygame.Surface(arrow_size)
arrow.fill(brown)
arrow_pos = pygame.Rect((random.randrange(0, 800), 0), arrow_size)

part = pygame.Surface((4, 4))
part.fill(brown)
part_pos = []

speed = 3
parts = 5

pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(green)
    if arrow_pos[1] >= 600:
        for i in range(parts):
            part_pos.append(arrow_pos.copy())
        arrow_pos = pygame.Rect((random.randrange(0, 800), random.randrange(0, 5)), arrow_size)
    else:
        arrow_pos.move_ip(0, speed)
        screen.blit(arrow, arrow_pos)
    for i in part_pos:

        if i[1] <= 575:
            part_pos = []
            break
        i.move_ip(random.randrange(-5, 6), random.randrange(-2, 0))
        screen.blit(part, i)
    time.sleep(.01)
    pygame.display.flip()
