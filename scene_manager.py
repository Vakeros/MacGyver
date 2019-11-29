from game import *


class SceneManager:
    scenes = [game]
    currentScene = 0
    @staticmethod
    def loadScene(Pid):
        SceneManager.scenes[SceneManager.currentScene].unload()
        SceneManager.currentScene = Pid
        SceneManager.scenes[SceneManager.currentScene].init()

    @staticmethod
    def update(screen):
        SceneManager.scenes[SceneManager.currentScene].update(screen)
