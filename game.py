from player import *
from world import *
from items import *
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
        if items.pickItemAt(game.player.getPositionCase()):
            game.player.pickUpItem()
        if world.getSpriteAt(game.player.getPositionCase()[0], game.player.getPositionCase()[1]) == "4":
            if items.count == game.player.inventory:
                print("win")
            else:
                print("items missing")
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
        print("unload")


