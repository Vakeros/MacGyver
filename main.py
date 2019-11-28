import pygame
from scene_manager import *

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
SceneManager.update(screen)
player = pygame.image.load('MacGyver.png').convert()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    pygame.display.flip()
    clock.tick(60)


