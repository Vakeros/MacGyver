import sys
from world import *
from scene_manager import *
from pygame.locals import *
pygame.init()
pygame.display.init()

size = width, height = 20*15, 20*15
screen = pygame.display.set_mode(size)
sceneManager.loadScene(1)  # load main game
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and sceneManager.currentScene == 0:
            if event.key == pygame.K_DOWN:
                game.player.setPosition("DOWN")
            if event.key == pygame.K_UP:
                game.player.setPosition("UP")
            if event.key == pygame.K_LEFT:
                game.player.setPosition("LEFT")
            if event.key == pygame.K_RIGHT:
                game.player.setPosition("RIGHT")
    screen.fill((0, 0, 0))
    sceneManager.update(screen)
    pygame.display.flip()
    clock.tick(60)


