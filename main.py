"""main"""
import sys
import pygame
from classes.scene_manager import SceneManager
from classes.game import Game
pygame.init()
pygame.display.init()

SIZE = WIDTH, HEIGHT = 20*15, 20*15
SCREEN = pygame.display.set_mode(SIZE)
SceneManager.load_scene(1)  # load main game
CLOCK = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and SceneManager.currentScene == 0:
            if event.key == pygame.K_DOWN:
                Game.player.set_position("DOWN")
            if event.key == pygame.K_UP:
                Game.player.set_position("UP")
            if event.key == pygame.K_LEFT:
                Game.player.set_position("LEFT")
            if event.key == pygame.K_RIGHT:
                Game.player.set_position("RIGHT")
    SCREEN.fill((0, 0, 0))
    SceneManager.update(SCREEN)
    pygame.display.flip()
    CLOCK.tick(60)

