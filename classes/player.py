"""player"""
import pygame
from classes.world import World


class Player:
    """player"""
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load('ressources/textures/MacGyver.png'),
                                             (20, 20))
        self.pos_x = 0
        self.pos_y = 0
        self.case_x = 0
        self.case_y = 0
        self.inventory = 0
        print("init player")

    # set position and check collider
    def set_position(self, direction):
        """change player position"""
        if direction == "DOWN":
            if not World.is_solid(World.get_sprite_at(self.case_x, self.case_y+1)):
                self.case_y += 1
                self.pos_y += 20
        elif direction == "UP":
            if not World.is_solid(World.get_sprite_at(self.case_x, self.case_y-1)):
                self.case_y -= 1
                self.pos_y -= 20
        elif direction == "LEFT":
            if not World.is_solid(World.get_sprite_at(self.case_x-1, self.case_y)):
                self.case_x -= 1
                self.pos_x -= 20
        elif direction == "RIGHT":
            if not World.is_solid(World.get_sprite_at(self.case_x+1, self.case_y)):
                self.case_x += 1
                self.pos_x += 20

    def get_position(self):
        """get player position"""
        return self.pos_x, self.pos_y

    def get_position_case(self):
        """get player position in case"""
        return self.case_x, self.case_y

    def pick_up_item(self):
        """take items"""
        self.inventory += 1
