import pygame
from monster import Monster


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.monster_group = monster_group

        blue_image = pygame.image.load("assets/blue_monster.png")
        green_image = pygame.image.load("assets/green_monster.png")
        purple_image = pygame.image.load("assets/purple_monster.png")
        yellow_image = pygame.image.load("assets/yellow_monster.png")

        self.all_monsters = [blue_image,
                             green_image, purple_image, yellow_image]

    def start_new_level(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(Monster(100, 140, self.all_monsters[0], 0))
            self.monster_group.add(Monster(200, 240, self.all_monsters[1], 1))
            self.monster_group.add(Monster(300, 340, self.all_monsters[2], 2))
            self.monster_group.add(Monster(400, 440, self.all_monsters[3], 3))
