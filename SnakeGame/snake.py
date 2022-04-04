import pygame
import random

class Game:
    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    pygame.display.update()

    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    x1 = 200
    y1 = 150
    x1_change = 0
    y1_change = 0
    clock = pygame.time.Clock()
    endgame = False


    class snake:
        length = 1
        tail = []


    class point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    s = snake()
    fruit = point(random.randint(1, 39) * 10, random.randint(1, 29) * 10)
    while not endgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if (snake.length == 1 or x1_change != 10):
                        x1_change = -10
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if (snake.length == 1 or x1_change != -10):
                        x1_change = 10
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if (snake.length == 1 or y1_change != 10):
                        y1_change = -10
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if (snake.length == 1 or y1_change != -10):
                        y1_change = 10
                        x1_change = 0
        x1 += x1_change
        y1 += y1_change

        # fruit mechanics
        pygame.draw.rect(dis, red, [fruit.x, fruit.y, 10, 10])
        if (x1 == fruit.x and y1 == fruit.y):
            pygame.draw.rect(dis, black, [fruit.x, fruit.y, 10, 10])
            fruit = point(random.randint(1, 39) * 10, random.randint(1, 29) * 10)
            pygame.draw.rect(dis, red, [fruit.x, fruit.y, 10, 10])
            snake.length += 1

        # Snake Movement
        if (len(snake.tail) > 0 and (snake.tail[-1].x != x1 or snake.tail[-1].y != y1)):
            snake.tail.append(point(x1, y1))
        if (len(snake.tail) == 0):
            snake.tail.append(point(x1, y1))
        if (snake.length < len(snake.tail)):
            old = snake.tail[0]
            pygame.draw.rect(dis, black, [old.x, old.y, 10, 10])
            del snake.tail[0]
        for i in range(len(snake.tail)):
            print(i)
            new = snake.tail[i]
            pygame.draw.rect(dis, blue, [new.x, new.y, 10, 10])

        # Game Ends
        if (x1 >= 400 or y1 >= 300 or x1 < 0 or y1 < 0):
            endgame = True
        for i in range(len(snake.tail) - 1):
            if (x1 == snake.tail[i].x and y1 == snake.tail[i].y):
                endgame = True
        pygame.display.update()
        clock.tick(20)
pygame.quit()
quit()
