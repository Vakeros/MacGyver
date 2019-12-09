"""world textures , collider ..."""

import pygame


class World:
    """world"""
    lvl = []
    nbCul = 20
    nbLines = 20
    Textures = []
    solidSprite = [2, 3, 4]

    @staticmethod
    def load():
        """load"""
        with open("ressources/maps/lvl1.txt", "r") as file:
            for line in file:
                t_line = []
                line = line.split(",")
                for sprite_id in line:
                    if sprite_id != '\n':
                        t_line.append(sprite_id)
                World.lvl.append(t_line)
        World.Textures = World.load_textures()

    @staticmethod
    def load_textures():
        """load textures"""
        image = pygame.image.load("ressources/textures/tiles.png").convert()
        line = []
        for pos_y in range(13):
            for pos_x in range(20):
                rect = (pos_x * 20, pos_y * 20, 20, 20)
                line.append(image.subsurface(rect))
        return line

    @staticmethod
    def update(screen):
        """update"""
        pos_x, pos_y = 0, 0
        for i in World.lvl:
            for k in i:
                if k != "G":
                    screen.blit(World.Textures[int(k)], (pos_x, pos_y))
                else:
                    screen.blit(World.Textures[1], (pos_x, pos_y))
                    screen.blit(pygame.transform.scale(
                        pygame.image.load('ressources/textures/Gardien.png'),
                        (20, 20)), (pos_x, pos_y))
                pos_x += 20
            pos_y += 20
            pos_x = 0

    @staticmethod
    def get_sprite_at(p_x, p_y):
        """get sprite at coord (case_pos)"""
        return World.lvl[p_y][p_x]

    @staticmethod
    def is_solid(sprite):
        """check if sprite id is solid for coll"""
        for i in World.solidSprite:
            if sprite != "G":
                if i == int(sprite):
                    return True
        return False

    @staticmethod
    def get_lvl():
        """return table content id and coord of sprite"""
        return World.lvl
