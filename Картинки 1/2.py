import pygame
from pygame.draw import *

pygame.init()






FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (0, 0, 255), (0, 0, 400, 200))
rect(screen, (255, 255, 0), (0, 200, 400, 200))
rect(screen, (150, 75, 0), (75, 150, 100, 75))
polygon(screen, (255, 0, 0), [(75, 150), (125, 100), (175, 150), (75, 150)])
rect(screen, (100, 100, 255), (95, 175, 25, 25))
rect(screen, (0, 0, 0), (140, 175, 20, 50))
circle(screen, (255, 255, 0), (50, 50), 30)
circle(screen, (0, 0, 0), (220, 50), 31)
circle(screen, (255, 255, 255), (220, 50), 30)
circle(screen, (0, 0, 0), (240, 50), 31)
circle(screen, (255, 255, 255), (240, 50), 30)
circle(screen, (0, 0, 0), (260, 50), 31)
circle(screen, (255, 255, 255), (260, 50), 30)
circle(screen, (0, 0, 0), (280, 50), 31)
circle(screen, (255, 255, 255), (280, 50), 30)
circle(screen, (0, 0, 0), (230, 70), 31)
circle(screen, (255, 255, 255), (230, 70), 30)
circle(screen, (0, 0, 0), (250, 70), 31)
circle(screen, (255, 255, 255), (250, 70), 30)
rect(screen, (160, 75, 0), (320, 175, 20, 75))
circle(screen, (0, 0, 0), (330, 140), 31)
circle(screen, (0, 255, 0), (330, 140), 30)
circle(screen, (0, 0, 0), (345, 155), 31)
circle(screen, (0, 255, 0), (345, 155), 30)
circle(screen, (0, 0, 0), (315, 155), 31)
circle(screen, (0, 255, 0), (315, 155), 30)
circle(screen, (0, 0, 0), (330, 170), 31)
circle(screen, (0, 255, 0), (330, 170), 30)
circle(screen, (0, 0, 0), (345, 185), 31)
circle(screen, (0, 255, 0), (345, 185), 30)
circle(screen, (0, 0, 0), (315, 185), 31)
circle(screen, (0, 255, 0), (315, 185), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
