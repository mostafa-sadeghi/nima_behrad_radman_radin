from pygame.sprite import Sprite
import pygame
import random


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = random.randint(1, 5)
        self.type = monster_type

        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def update(self):
        pass
