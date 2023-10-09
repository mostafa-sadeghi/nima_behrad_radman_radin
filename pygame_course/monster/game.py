import pygame
from config import *
from monster import Monster
from random import randint


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

        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.all_monsters[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.bottom = 100
        self.target_monster_rect.centerx = WINDOW_WIDTH/2

    def draw(self, screen):
        # TODO
        # display game score on the screen
        # display game level on the screen
        # display player lives on the screen
        screen.blit(self.target_monster_image, self.target_monster_rect)

    def start_new_level(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster(randint(0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[0], 0))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[1], 1))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[2], 2))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT - 164), self.all_monsters[3], 3))

        # TODO  play start new level sound
