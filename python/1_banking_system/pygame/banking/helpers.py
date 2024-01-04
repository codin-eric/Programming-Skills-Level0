import pygame
from constants import FAMILY_FONT_NAME


def draw_text(screen, msg, size, color, x_text, y_text):
    """ Function to make easyer to draw text
    screen: pygame screen buffer (Where the text is going to be displayed)
    msg: string of what you want to say
    color: text color
    x_text: x position of your text
    y_text: y position of your text
    """
    font_name = pygame.font.match_font(FAMILY_FONT_NAME)
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(
        msg, True, color
    )
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x_text, y_text)
    screen.blit(text_surface, text_rect)


def circle_surf(radius, color):
    surf = pygame.Surface((radius*2, radius*2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf
