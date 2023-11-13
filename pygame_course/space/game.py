import pygame


class Game:
    def __init__(self, player, enemy_group, player_bullet_group, enemy_bullet_group) -> None:
        self.score = 0
        self.level_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group
        self.font = pygame.font.Font("assets/Facon.ttf")

