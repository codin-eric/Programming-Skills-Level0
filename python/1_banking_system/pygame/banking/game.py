import pygame
from constants import SCREEN_RESOLUTION, DARKGREY, WHITE, BLACK, RED, DARKRED

from game_console import Chibi, Basic_button
from helpers import draw_text


pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption("garden")
clock = pygame.time.Clock()


def quitgame():
    pygame.quit()
    quit()


def intro() -> None:
    running = True
    intro = Chibi()
    transition = 0

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN and not transition:
                transition = 0.5

        if transition:
            intro.set_pos(-transition, 0)
            transition += 1
            if transition >= 23:
                print(intro.pos)
                return None

        # Draw
        screen.fill(DARKGREY)
        intro.move()

        intro.draw(screen)

        if not transition:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (0, SCREEN_RESOLUTION[1] / 1.5 - 25, SCREEN_RESOLUTION[0], 100),
            )
            draw_text(
                screen,
                "Presiona cualquier tecla para comenzar",
                80,
                WHITE,
                SCREEN_RESOLUTION[0] / 8,
                SCREEN_RESOLUTION[1] / 1.5,
            )

        pygame.display.update()
        clock.tick(60)


def login_scene():
    chibi = Chibi()
    chibi.set_pos(-265, 0)
    name_btn = Basic_button(
        "Name",
        (SCREEN_RESOLUTION[0] * 0.75, SCREEN_RESOLUTION[1] * 0.25),
        (200, 50),
        DARKRED,
        RED,
        None,
    )
    pass_btn = Basic_button(
        "Password",
        (SCREEN_RESOLUTION[0] * 0.75, SCREEN_RESOLUTION[1] * 0.50),
        (200, 50),
        DARKRED,
        RED,
        None,
    )
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitgame()

        # Move
        chibi.move()
        # Draw
        screen.fill(DARKGREY)
        chibi.draw(screen)
        name_btn.draw(screen)
        pass_btn.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    intro()
    login_scene()
