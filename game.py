from player import *
import scene_manager as sm
from world import *
from items import *
from gameOver import over


class game:
    @staticmethod
    def init():
        print("init")
        game.player = Player()
        world.load()
        items.init()

    @staticmethod
    def update(screen):
        world.update(screen)
        items.update(screen)
        events = pygame.event.get()
        screen.blit(game.player.sprite, game.player.getPosition())
        allKeys = pygame.key.get_pressed()
        font = pygame.font.SysFont("comicsansms", 12)
        screen.blit(font.render("{} items sur {} .".format(game.player.inventory, items.count),
                                True, (0, 0, 0)), (200, 1))
        if items.pickItemAt(game.player.getPositionCase()):
            game.player.pickUpItem()
        if world.getSpriteAt(game.player.getPositionCase()[0], game.player.getPositionCase()[1]) == "G":
            if items.count == game.player.inventory:
                sm.sceneManager.loadScene(2)
                over.setText("Vous avez gagnez")
            else:
                sm.sceneManager.loadScene(2)
                over.setText("GameOver vous n'avez récupéré les items")
        # player control"
        """
        if allKeys[pygame.K_LEFT]:
            game.player.setPosition((game.player.getPosition()[0] - game.player.getSpeed(), game.player.getPosition()[1]))
        elif allKeys[pygame.K_RIGHT]:
            game.player.setPosition((game.player.getPosition()[0] + game.player.getSpeed(), game.player.getPosition()[1]))
        if allKeys[pygame.K_UP]:
            game.player.setPosition((game.player.getPosition()[0], game.player.getPosition()[1] - game.player.getSpeed()))
        elif allKeys[pygame.K_DOWN]:
            game.player.setPosition((game.player.getPosition()[0], game.player.getPosition()[1] + game.player.getSpeed()))
        """

    @staticmethod
    def unload():
        items.unload()
        print("unload")
