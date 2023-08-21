import pygame
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dragon Game")

dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)
dragon_right_rect = dragon_left.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

font = pygame.font.Font("minecraft.ttf", 62)
# font = pygame.font.SysFont("Arial.ttf", 62)
title = font.render("Dragon Game", True, (0, 255, 0))
title_rect = title.get_rect()
title_rect.top = 0
title_rect.centerx = WINDOW_WIDTH/2


player = dragon_right
player_rect = player.get_rect()
player_rect.midleft = (20, WINDOW_HEIGHT/2)

# TODO   لود کردن عکس غذای دراگون
# مکان غذای دراگون در خارج از سمت راست صفحه
# و ارتفاع آن در موقعیت تصادفی قرار داده شود


FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_rect.top > 128:
        player_rect.y -= 5

    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon_left, dragon_left_rect)
    display_surface.blit(dragon_right, dragon_right_rect)
    pygame.draw.line(display_surface, WHITE, (0, 128), (WINDOW_WIDTH, 128), 4)
    display_surface.blit(title, title_rect)
    display_surface.blit(player, player_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
