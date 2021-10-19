import pygame
from pygame.draw import *
from random import randint
import math as m

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1380, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
for i in range(randint(6, 12)):
    x = randint(100, 1200)
    y = randint(100, 800)
    r = randint(50, 70)
    color = COLORS[randint(0, 5)]
    balls.append([color, x, y, r])
l = len(balls)

v = []
for i in range(l):
    vx = randint(-5, 5)
    vy = randint(-5, 5)
    v.append([vx, vy])

x1 = randint(100, 1000)
y1 = randint(100, 800)
p = 25


def new_ball(color, x, y, r):
    circle(screen, color, (x, y), r)


def end(d):
    if d == 1:
        polygon(screen, (0, 0, 0), [(0, 0), (1380, 0), (1380, 900), (0, 900)])
        font = pygame.font.Font(None, 100)
        win = font.render('победа', True, (255, 0, 0))
        screen.blit(win, (560, 400))
        font = pygame.font.Font(None, 100)
        schet1 = font.render('счет:', True, (255, 0, 0))
        schet2 = font.render(str(count), True, (255, 0, 0))
        screen.blit(schet2, (760, 500))
        screen.blit(schet1, (560, 500))
    if d == 0:
        polygon(screen, (0, 0, 0), [(0, 0), (1380, 0), (1380, 900), (0, 900)])
        font = pygame.font.Font(None, 100)
        defeat = font.render('поражение', True, (255, 0, 0))
        screen.blit(defeat, (500, 400))
        font = pygame.font.Font(None, 100)
        schet1 = font.render('счет:', True, (255, 0, 0))
        schet2 = font.render(str(count), True, (255, 0, 0))
        screen.blit(schet2, (700, 500))
        screen.blit(schet1, (500, 500))


def score(count):
    font = pygame.font.Font(None, 100)
    text = font.render(str(count), True, RED)
    screen.blit(text, (50, 100))


def qw(s):
    if s > 0:
        font = pygame.font.Font(None, 100)
        death = font.render('x', True, RED)
        screen.blit(death, (1000, 100))
    if s > 1:
        screen.blit(death, (1100, 100))
    if s > 2:
        screen.blit(death, (1200, 100))


def click(event):
    global count, n, x1, y1, h, s
    for i in range(l):
        if (balls[i][1] - event.pos[0]) ** 2 + (balls[i][2] - event.pos[1]) ** 2 < (balls[i][3]) ** 2:
            count += 1
            balls.pop(i)
            x = randint(100, 700)
            y = randint(100, 500)
            r = randint(10, 15) + randint(40, 60) * m.exp(-n / 40)
            color = COLORS[randint(0, 5)]
            balls.append([color, x, y, r])
            n += 1
            s -= 1
        elif (x1 - event.pos[0]) ** 2 + (y1 - event.pos[1]) ** 2 < p ** 2:
            count += randint(-7, 9)
            x1 = randint(100, 1000)
            y1 = randint(100, 800)
            h += 1
            s -= 1
    s += 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score(0)
count = 0
n = 0
t = 0
h = 0
s = 0
d = -1
time = 0

while not finished:
    if d == -1:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
        for i in range(l):
            color, x, y, r = balls[i]
            new_ball(color, x, y, r)
        for i in range(l):
            balls[i][1] += v[i][0]
            balls[i][2] += v[i][1]
            if balls[i][1] - balls[i][3] < 0 or balls[i][1] + balls[i][3] > 1380:
                v[i][0] = -v[i][0]
            if balls[i][2] - balls[i][3] < 65 or balls[i][2] + balls[i][3] > 835:
                v[i][1] = -v[i][1]
        circle(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (x1, y1), p)
        p = (25 + 25 * m.sin(t / 5)) * m.exp(-h / 40)
        t += 1
        score(count)
        qw(s)
        if count == 10:
            d = 1
        if s > 2:
            d = 0
        end(d)
        pygame.display.update()
        screen.fill(BLACK)

pygame.quit()
#123456