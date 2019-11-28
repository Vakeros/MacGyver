import pygame
class game:
    @staticmethod
    def init():
        print("init")

    @staticmethod
    def update(screen):
        print("update game")
        player = pygame.image.load('MacGyver.png').convert()
        screen.blit(player, (0, 0))

    @staticmethod
    def unload():
        print("unload")