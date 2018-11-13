import sys
import pygame
import random
import time

blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))
screen.fill(black)

rain = pygame.Surface((3, 10))
rain.fill(blue)
rain_pos = pygame.Rect((random.randrange(1, 800), 0), (1, 5))
rain_list = [rain_pos]
rain_list_vis = [rain]

speed = 3
count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    screen.fill(black)
    for i in range(len(rain_list)):
        rain_list[i].move_ip(0, speed)
        screen.blit(rain_list_vis[i], rain_list[i])
    rain.fill(blue)
    rain_list.append(pygame.Rect((random.randrange(1, 800), 0), (1, 5)))
    rain_list_vis.append(pygame.Surface((random.randrange(1, 3), random.randrange(5, 15))))
    count += 1
    rain_list_vis[count].fill(blue)
    time.sleep(.005)
    pygame.display.flip()