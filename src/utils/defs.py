import pygame

pygame.init()
pygame.font.init()

SCREEN_SIZE = WIDTH = HEIGHT = 600

font = pygame.font.SysFont('candara', 30, True)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Game')

pygame.key.set_repeat(100, 15)
