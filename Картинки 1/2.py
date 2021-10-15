import pygame
import pygame.draw as dr

"""Задание цветов"""
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BROWN = (150, 75, 0)

"""Размеры экрана"""
height = 500
width = 500

"""Инициализация pygame и конфигурирование дисплея"""
pygame.init()
FPS = 30
screen = pygame.display.set_mode((height, width))

"""Поправочные коэффициенты масштабирования"""
kx = width / 400
ky = height / 400
k = kx


def house(x, y, size):
    """
    Отрисовывает домик с заданными координатами и линейным размером
    :param x: x-положение левого верхнего края домика
    :param y: y-положение левого верхнего края домика
    :param size: пропорциаонльные размеры домика
    """
    dr.rect(screen, (150, 75, 0), (x * kx, y * ky, size * kx, 0.75 * size * ky))

    dr.polygon(screen, RED,
               [(x * kx, y * ky), ((x + size / 2) * kx, (y - size / 2) * ky),
                ((size + x) * kx, y * ky)])

    dr.rect(screen, (100, 100, 255), ((x + size / 5) * kx, (y + size / 4) * ky, size * kx / 4, size * ky / 4))
    dr.rect(screen, (0, 0, 0), ((x + 0.75 * size) * kx, (y + size / 4) * ky, size * kx / 5, size * ky / 2))


def sun():
    """
    Отрисовывает солнце в левом верхнем углу экрана
    """
    dr.circle(screen, YELLOW, (50 * kx, 50 * ky), 30 * k)


def background(sky_color, surf_color):
    """
    Отрисовывает небо и землю соответвующих цветов в соотношении 1 : 1 на экране
    :param sky_color: цвет неба
    :param surf_color: цвет земли
    """
    dr.rect(screen, sky_color, (0, 0, width, height // 2))
    dr.rect(screen, surf_color, (0, height // 2, width, height))


def leafage():
    """
    Отрисовывает листву на дереве
    """
    dr.circle(screen, (0, 0, 0), (330 * kx, 140 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (330 * kx, 140 * ky), 30 * k)
    dr.circle(screen, (0, 0, 0), (345 * kx, 155 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (345 * kx, 155 * ky), 30 * k)
    dr.circle(screen, (0, 0, 0), (315 * kx, 155 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (315 * kx, 155 * ky), 30 * k)
    dr.circle(screen, (0, 0, 0), (330 * kx, 170 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (330 * kx, 170 * ky), 30 * k)
    dr.circle(screen, (0, 0, 0), (345 * kx, 185 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (345 * kx, 185 * ky), 30 * k)
    dr.circle(screen, (0, 0, 0), (315 * kx, 185 * ky), 31 * k)
    dr.circle(screen, (0, 255, 0), (315 * kx, 185 * ky), 30 * k)


def tree():
    """
    Отрисовывает дерево в правой части экрана
    """
    dr.rect(screen, (160, 75, 0), (320 * kx, 175 * ky, 20 * kx, 75 * ky))
    leafage()


def clouds():
    """
    Отрисовывает облака на небе в вехней части экрана
    """
    dr.circle(screen, WHITE, (220 * kx, 50 * ky), 30 * k)
    dr.circle(screen, BLACK, (240 * kx, 50 * ky), 31 * k)
    dr.circle(screen, WHITE, (240 * kx, 50 * ky), 30 * k)
    dr.circle(screen, BLACK, (260 * kx, 50 * ky), 31 * k)
    dr.circle(screen, WHITE, (260 * kx, 50 * ky), 30 * k)
    dr.circle(screen, BLACK, (280 * kx, 50 * ky), 31 * k)
    dr.circle(screen, WHITE, (280 * kx, 50 * ky), 30 * k)
    dr.circle(screen, BLACK, (230 * kx, 70 * ky), 31 * k)
    dr.circle(screen, WHITE, (230 * kx, 70 * ky), 30 * k)
    dr.circle(screen, BLACK, (250 * kx, 70 * ky), 31 * k)
    dr.circle(screen, WHITE, (250 * kx, 70 * ky), 30 * k)


"""Отрисовка целого изображения"""
background(BLUE, YELLOW)
house(70, 200, 150)
sun()
clouds()
tree()

"""Вывод изображения на экран с помощью pygame"""
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
