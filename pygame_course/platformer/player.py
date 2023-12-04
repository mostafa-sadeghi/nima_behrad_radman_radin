import pygame
from pygame.sprite import Sprite
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        image = pygame.image.load('assets/boy/Idle (1).png')
        self.image = pygame.transform.scale(image, (image.get_width() * 0.2, image.get_height() * 0.2))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 5
        self.vely = 0


    def update(self,screen):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed

        self.vely += 1
        dy += self.vely

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
            
        pygame.draw.rect(screen, (10,245,220), self.rect, 4)