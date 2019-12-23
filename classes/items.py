"""items"""
import random
from datetime import datetime
import pygame
from classes.world import World


class Items:
    """Items"""
    list = []
    sprite = [
                pygame.image.load('ressources/textures/aiguille.png'),
                pygame.image.load('ressources/textures/seringue.png'),
                pygame.image.load('ressources/textures/ether.png')
             ]

    def __init__(self, position):
        self.position = position
        self.in_world = True

    @staticmethod
    def init():
        """init"""
        Items.count = 3
        random.seed(datetime.now())
        Items.generate_items()

    @staticmethod
    def unload():
        """unload"""
        Items.list.clear()

    @staticmethod
    def generate_items():
        """generate items"""
        Items.list = []
        possible_position = []
        for i in range(Items.count):
            pos_x, pos_y = 0, 0
            for j in World.get_lvl():
                pos_x = 0
                for k in j:
                    if not World.is_solid(k):
                        possible_position.append((pos_x, pos_y))
                    pos_x += 1
                pos_y += 1
        for i in range(Items.count):
            rng = random.randrange(0, len(possible_position))
            Items.list.append(Items(possible_position[rng]))
            possible_position.pop(rng)

    # check if player is in item position
    @staticmethod
    def pick_item_at(pos):
        """pick up items"""
        for i in Items.list:
            if i.position == pos and i.in_world:
                i.in_world = False
                return True
        return False

    # draw Items
    @staticmethod
    def update(screen):
        """update"""
        for i in range(len(Items.list)):
            if Items.list[i].in_world:
                screen.blit(pygame.transform.scale(Items.sprite[i], (20, 20)),
                            (Items.list[i].position[0]*20, Items.list[i].position[1]*20))
