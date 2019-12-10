"""Game"""
import pygame
from classes.player import Player
from classes.items import Items
from classes import scene_manager as sm
from classes.world import World
from classes.game_over import Over


class Game:
    """Game"""
    @staticmethod
    def init():
        """init"""
        Game.player = Player()
        World.load()
        Items.init()

    @staticmethod
    def update(screen):
        """update"""
        World.update(screen)
        Items.update(screen)
        screen.blit(Game.player.sprite, Game.player.get_position())
        font = pygame.font.SysFont("comicsansms", 12)
        screen.blit(font.render("{} Items sur {} .".format(Game.player.inventory, Items.count),
                                True, (0, 0, 0)), (200, 1))
        if Items.pick_item_at(Game.player.get_position_case()):
            Game.player.pick_up_item()
        if World.get_sprite_at(Game.player.get_position_case()[0],
                             Game.player.get_position_case()[1]) == "G":
            if Items.count == Game.player.inventory:
                sm.SceneManager.load_scene(2)
                Over.set_text("Vous avez gagnez")
            else:
                sm.SceneManager.load_scene(2)
                Over.set_text("GameOver vous n'avez pas récupéré les Items")

    @staticmethod
    def unload():
        """unload"""
        Items.unload()
        print("unload")
