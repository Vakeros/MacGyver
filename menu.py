import pygame
import scene_manager as sm


class menu:
    @staticmethod
    def init():
        menu.font = pygame.font.SysFont("comicsansms", 12)
        menu.text = menu.font.render("Ceci est un menu vide avec la pire police qui existe.",
                                     True, (255, 255, 255))
        menu.text2 = menu.font.render(" Appuyer sur espace pour jouer",
                                      True, (255, 255, 255))
        print("init")

    @staticmethod
    def update(screen):
        screen.blit(menu.text, (10, 40))
        screen.blit(menu.text2, (60, 140))
        allKeys = pygame.key.get_pressed()
        if allKeys[pygame.K_SPACE]:
           sm.sceneManager.loadScene(0)

    @staticmethod
    def unload():
        print("unload")
