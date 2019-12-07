import pygame
import scene_manager as sm


class over:
    @staticmethod
    def init():
        over.font = pygame.font.SysFont("comicsansms", 12)
        over.text = over.font.render("GameOver",
                                     True, (255, 255, 255))
        print("init")

    @staticmethod
    def setText(pText):
        over.text = over.font.render(pText,
                                     True, (255, 255, 255))

    @staticmethod
    def update(screen):
        screen.blit(over.text, (60, 120))
        screen.blit(over.font.render(("Toujours en comicsansms ..."), True, (255, 255, 255)), (60, 140))
        allKeys = pygame.key.get_pressed()
        if allKeys[pygame.K_SPACE]:
            sm.sceneManager.loadScene(1)

    @staticmethod
    def unload():
        print("unload")
