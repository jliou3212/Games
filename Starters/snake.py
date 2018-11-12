import pygame
import sys
import time
import random
pygame.init()

directionx, directiony = 0, 0
res = width, height = 800, 600
screen = pygame.display.set_mode(res)
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

candy = pygame.Surface((10, 10))
candy.fill(red)
candy_pos = pygame.Rect((random.randrange(0, 800, 10), random.randrange(0, 600, 10)), (10, 10))

tail_len = 0
tails = []
snake_tail_pos = pygame.Rect((200, 200), (10, 10))
tails.append(snake_tail_pos)

snake = pygame.Surface((10, 10))
snake.fill(white)
snake_head_pos = pygame.Rect((200, 200), (10, 10))
speed = 10


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_d:
                if directionx >= 0:
                    directionx = speed
                    directiony = 0
            if event.key == pygame.K_a:
                if directionx <= 0:
                    directionx = -speed
                    directiony = 0
            if event.key == pygame.K_w:
                if directiony <= 0:
                    directiony = -speed
                    directionx = 0
            if event.key == pygame.K_s:
                if directiony >= 0:
                    directiony = speed
                    directionx = 0

    screen.fill(black)
    for i in range(tail_len, 0, -1):
        tails[i] = tails[i-1].copy()
    tails[0] = snake_head_pos.copy()
    tails[0] = snake_head_pos.copy()

    snake_head_pos.move_ip(directionx, directiony)

    if snake_head_pos == candy_pos:
        candy_pos = pygame.Rect((random.randrange(0, 800, 10), random.randrange(0, 600, 10)), (10, 10))
        tail_len += 1
        tails.append(snake_tail_pos)

    if snake_head_pos[0] > width or snake_head_pos[0] < 0 or snake_head_pos[1] > height or snake_head_pos[1] < 0:
        sys.exit()

    if snake_head_pos in tails[1:]:
        sys.exit()
    for i in tails:
        screen.blit(snake, i)
    screen.blit(candy, candy_pos)
    screen.blit(snake, snake_head_pos)

    time.sleep(.05)
    pygame.display.flip()



