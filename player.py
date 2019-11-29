import pygame
from world import *


class Player:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load('MacGyver.png'), (20, 20))
        self.X = 0
        self.Y = 0
        self.caseX = 0
        self.caseY = 0
        print("init player")

    def setPosition(self, direction):
        if direction == "DOWN":
            if world.lvl[self.caseY+1][self.caseX] == "0":
                self.caseY += 1
                self.Y += 20
        elif direction == "UP":
            if world.lvl[self.caseY-1][self.caseX] == "0":
                self.caseY -= 1
                self.Y -= 20
        elif direction == "LEFT":
            if world.lvl[self.caseY][self.caseX-1] == "0":
                self.caseX -= 1
                self.X -= 20
        elif direction == "RIGHT":
            if world.lvl[self.caseY][self.caseX+1] == "0":
                self.caseX += 1
                self.X += 20

    def getPosition(self):
        return (self.X, self.Y)

    def getSpeed(self):
        return self.speed
