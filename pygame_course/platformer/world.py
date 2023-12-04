import pygame
from constants import *

class World:
    def __init__(self, tile_map):
        self.image = pygame.image.load("assets/background.png")
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(topleft = (0,0))

    def draw(self,screen):
        screen.blit(self.image, self.rect)