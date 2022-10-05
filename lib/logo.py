import pygame

LOGO_SPEED = 3


def bounce_if_required(speed_tuple, position_rect):
    if position_rect.left <= 0:
        speed_tuple[0] = LOGO_SPEED
    elif position_rect.right >= SCREEN_WIDTH:
        speed_tuple[0] = -LOGO_SPEED

    # Bovenkant van het scherm geraakt?
    if position_rect.top <= 0:
        speed_tuple[1] = LOGO_SPEED
    # Onderkant van het scherm geraakt?
    elif position_rect.bottom >= SCREEN_HEIGHT:
        speed_tuple[1] = -LOGO_SPEED
