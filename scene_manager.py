from game import *
from menu import menu
from gameOver import over
class sceneManager:
    scenes = [game, menu, over]
    currentScene = 0
    @staticmethod
    def loadScene(Pid):
        sceneManager.scenes[sceneManager.currentScene].unload()
        sceneManager.currentScene = Pid
        sceneManager.scenes[sceneManager.currentScene].init()

    @staticmethod
    def update(screen):
        sceneManager.scenes[sceneManager.currentScene].update(screen)

