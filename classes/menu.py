"""scene menu"""
import pygame
from classes import scene_manager as sm


class Menu:
    """menu"""
    def init():
        """init"""
        Menu.font = pygame.font.SysFont("comicsansms", 12)
        Menu.text = Menu.font.render("Ceci est un menu vide avec la pire police qui existe.",
                                     True, (255, 255, 255))
        Menu.text2 = Menu.font.render(" Appuyer sur espace pour jouer",
                                      True, (255, 255, 255))
        print("init")

    @staticmethod
    def update(screen):
        """update"""
        screen.blit(Menu.text, (10, 40))
        screen.blit(Menu.text2, (60, 140))
        all_keys = pygame.key.get_pressed()
        if all_keys[pygame.K_SPACE]:
            sm.SceneManager.load_scene(0)

    @staticmethod
    def unload():
        """unload"""
        print("unload")
