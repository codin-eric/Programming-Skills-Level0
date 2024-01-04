import pygame
from math import sin
from constants import (
    WHITE,
    BLACK,
    GREY,
    SCREEN_RESOLUTION,
    CHIBI_IMAGE_PATH,
)
from helpers import draw_text


ORD_OF_A = 97  # ASCII number of letter A
TILE_SIZE = 256


class Chibi:
    def __init__(self) -> None:
        image = pygame.image.load(CHIBI_IMAGE_PATH)
        self.base_img = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE * 2))
        self.pos = [
            SCREEN_RESOLUTION[0] / 2 - TILE_SIZE / 2,
            SCREEN_RESOLUTION[1] / 2 - TILE_SIZE * 2,
        ]
        self.hight = 0

    def set_pos(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def move(self):
        self.pos[1] = self.pos[1] + sin(self.hight)
        self.hight += 0.05

    def draw(self, screen):
        screen.blit(self.base_img, self.pos)


class Basic_button:
    def __init__(self, msg, pos, size, iddle_color, active_color, action):
        """Initialization of the basic button
        msg: String with what you want the button to display
        pos: tupple (x,y) of the button's position
        size: tupple (w,h) of the button's size
        iddle_color: button's color when is not active
        active_color: button's color when is hovered
        """

        self.msg = msg
        self.pos = pos
        self.size = size
        self.iddle_color = iddle_color
        self.active_color = active_color
        self.color = iddle_color
        self.action = action

    def do_action(self):
        mouse = pygame.mouse.get_pos()
        if (self.pos[0] + self.size[0]) > mouse[0] > self.pos[0] and (
            self.pos[1] + self.size[1]
        ) > mouse[1] > self.pos[1]:
            self.action()

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        if (self.pos[0] + self.size[0]) > mouse[0] > self.pos[0] and (
            self.pos[1] + self.size[1]
        ) > mouse[1] > self.pos[1]:
            self.color = self.active_color
        else:
            self.color = self.iddle_color

        pygame.draw.rect(
            screen, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1])
        )
        draw_text(
            screen,
            self.msg,
            20,
            WHITE,
            self.pos[0] + self.size[0] / 2,
            self.pos[1] + self.size[1] / 2,
        )
