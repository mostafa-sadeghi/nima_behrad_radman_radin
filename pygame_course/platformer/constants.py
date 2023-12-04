import pygame

screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
TILE_SIZE = 32

print(SCREEN_WIDTH/TILE_SIZE)
print(SCREEN_HEIGHT/TILE_SIZE)