"""scenes manager"""
from classes.game import Game
from classes.menu import Menu
from classes.game_over import Over


class SceneManager:
    """sceneManager"""
    @staticmethod
    def init():
        SceneManager.scenes = [Game, Menu, Over]
        SceneManager.currentScene = 0

    @staticmethod
    def load_scene(pid):
        """loadScene"""
        SceneManager.scenes[SceneManager.currentScene].unload()
        SceneManager.currentScene = pid
        SceneManager.scenes[SceneManager.currentScene].init()

    @staticmethod
    def update(screen):
        """update"""
        SceneManager.scenes[SceneManager.currentScene].update(screen)
