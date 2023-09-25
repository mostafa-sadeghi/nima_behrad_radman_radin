import pygame
from player import Player

from config import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

my_player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))
    my_player.draw(display_surface)
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)
