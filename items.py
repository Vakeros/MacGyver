import os
import random
from datetime import datetime
from world import *


class items:
    list = []
    sprite = pygame.image.load('MacGyver.png')

    def __init__(self, position):
        self.position = position
        self.inWorld = True

    @staticmethod
    def init():
        items.count = 10;
        random.seed(datetime.now())
        items.generateItems()

    @staticmethod
    def unload():
        items.list = []

    @staticmethod
    def generateItems():
        possiblePosition = []
        for i in range(items.count):
            x, y = 0, 0
            for j in world.getLvl():
                x = 0
                for k in j:
                    if not world.isSolid(k):
                        possiblePosition.append((x, y))
                    x += 1
                y += 1
        for i in range(items.count):
            rng = random.randrange(0, len(possiblePosition))
            items.list.append(items(possiblePosition[rng]))
            possiblePosition.pop(rng)

    # check if player is in item position
    @staticmethod
    def pickItemAt(pos):
        for i in items.list:
            if i.position == pos and i.inWorld:
                i.inWorld = False
                return True
        return False

    # draw items
    @staticmethod
    def update(screen):
        for i in range(len(items.list)):
            if items.list[i].inWorld:
                screen.blit(pygame.transform.scale(items.sprite, (20, 20)), (items.list[i].position[0]*20,
                                                                             items.list[i].position[1]*20))
