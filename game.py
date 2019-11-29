from player import *
from world import *
class game:
    @staticmethod
    def init():
        print("init")
        game.player = Player()
        world.load()
    @staticmethod
    def update(screen):
        world.update(screen)
        events = pygame.event.get()
        screen.blit(game.player.sprite, game.player.getPosition())
        allKeys = pygame.key.get_pressed()

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

def load_tile_table(filename, width, height):
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table
