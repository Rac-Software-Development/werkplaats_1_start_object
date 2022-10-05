import pygame
from pygame.sprite import Group, collide_rect

from logo import Logo

pygame.init()
GAME_SPEED = 60

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# Kleuren worden aangeven met een tuple van 3 getallen - rood, groen, blauw - tussen 0 en 255.
# 0, 0, 0 betekend geen kleurm, dus zwart.
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Werkplaats 1: PyGame")
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def quit_game_requested():
    halting = False
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
    return halting


logo = Logo()
while not quit_game_requested():
    canvas.fill(BACKGROUND_COLOR)
    logo.update(canvas)
    pygame.display.flip()
    clock.tick(GAME_SPEED)

print("Game over!")
