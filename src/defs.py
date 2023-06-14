import pygame

pygame.init()
pygame.font.init()

SCREEN_SIZE = WIDTH = HEIGHT = 600

font = pygame.font.SysFont('candara', 30, True)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Game')

pygame.key.set_repeat(100, 15)


_mx = 0
_my = 0


def update_mouse_pos():
    global _mx, _my
    _mx, _my = pygame.mouse.get_pos()


def mx():
    return _mx


def my():
    return _my
