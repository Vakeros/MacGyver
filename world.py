
import pygame
class world:
    lvl = []
    nbCul = 20
    nbLines = 20
    Textures = []
    solidSprite = [1, 2, 3]

    @staticmethod
    def load():
        texture = pygame.image.load("tiles.png").convert()
        with open("lvl1.md", "r") as file:
            for line in file:
                Tline = []
                for id in line:
                    if id != '\n':
                        Tline.append(id)
                world.lvl.append(Tline)
        world.Textures = world.load_tile_table("tiles.png", 20, 20)

    @staticmethod
    def load_tile_table(filename, width, height):
        image = pygame.image.load(filename).convert()
        image_width, image_height = image.get_size()
        for tile_x in range(0, round(image_width / width)):
            line = []
            for tile_y in range(0, round(image_height / height)):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))
        return line

    @staticmethod
    def update(screen):
        x, y = 0, 0
        for i in world.lvl:
            for k in i:
                if k != "G":
                    screen.blit(world.Textures[int(k)], (x, y))
                else:
                    screen.blit(pygame.transform.scale(pygame.image.load('Gardien.png'), (20, 20)), (x, y))
                x += 20
            y += 20
            x = 0

    @staticmethod
    def getSpriteAt(pX, pY):
        return world.lvl[pY][pX]

    @staticmethod
    def isSolid(sprite):
        for i in world.solidSprite:
            if sprite != "G":
                if i == int(sprite):
                    return True
        return False

    @staticmethod
    def getLvl():
        return world.lvl
