"""game Over"""
import pygame
from classes import scene_manager as sm


class Over:
    """game Over"""
    @staticmethod
    def init():
        """init"""
        Over.font = pygame.font.SysFont("comicsansms", 12)
        Over.text = Over.font.render("GameOver",
                                     True, (255, 255, 255))
        print("init")

    @staticmethod
    def set_text(ptext):
        """set screen text"""
        Over.text = Over.font.render(ptext,
                                     True, (255, 255, 255))

    @staticmethod
    def update(screen):
        """update"""
        screen.blit(Over.text, (60, 120))
        screen.blit(Over.font.render(("Toujours en comicsansms ..."), True,
                                     (255, 255, 255)), (60, 140))
        all_keys = pygame.key.get_pressed()
        if all_keys[pygame.K_SPACE]:
            sm.SceneManager.load_scene(1)

    @staticmethod
    def unload():
        """unload"""
        print("unload")
