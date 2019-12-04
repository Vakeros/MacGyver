

import pygame


class world:
    lvl = []
    nbCul = 20
    nbLines = 20
    Textures = []
    solidSprite = [2, 3, 4]

    @staticmethod
    def load():
        with open("lvl1.txt", "r") as file:
            for line in file:
                Tline = []
                line = line.split(",")
                for id in line:
                    if id != '\n':
                        Tline.append(id)
                world.lvl.append(Tline)
        world.Textures = world.loadTextures()

    @staticmethod
    def loadTextures():
        image = pygame.image.load("tiles.png").convert()
        line = []
        for y in range(13):
            for x in range(20):
                rect = (x * 20, y * 20, 20, 20)
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
                    screen.blit(world.Textures[1], (x, y))
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
