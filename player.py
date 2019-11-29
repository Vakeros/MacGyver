import pygame
from world import *


class Player:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load('MacGyver.png'), (20, 20))
        self.X = 0
        self.Y = 0
        self.caseX = 0
        self.caseY = 0
        self.inventory = 0
        print("init player")

    # set position and check collider
    def setPosition(self, direction):
        print("set")
        if direction == "DOWN":
            if not world.isSolid(world.getSpriteAt(self.caseX, self.caseY+1)):
                self.caseY += 1
                self.Y += 20
        elif direction == "UP":
            if not world.isSolid(world.getSpriteAt(self.caseX, self.caseY-1)):
                self.caseY -= 1
                self.Y -= 20
        elif direction == "LEFT":
            if not world.isSolid(world.getSpriteAt(self.caseX-1, self.caseY)):
                self.caseX -= 1
                self.X -= 20
        elif direction == "RIGHT":
            if not world.isSolid(world.getSpriteAt(self.caseX+1, self.caseY)):
                self.caseX += 1
                self.X += 20

    def getPosition(self):
        return (self.X, self.Y)

    def getPositionCase(self):
        return (self.caseX, self.caseY)

    def getSpeed(self):
        return self.speed

    def pickUpItem(self):
        self.inventory += 1
