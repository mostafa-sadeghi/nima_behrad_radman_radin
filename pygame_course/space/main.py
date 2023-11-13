import pygame
from player import Player
from constants import *
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
player = Player(player_bullet_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == K_SPACE:
                player.fire()
    screen.fill((0,0,0))
    player.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
