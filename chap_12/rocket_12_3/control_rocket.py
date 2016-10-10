from rocket import Rocket
from settings import Settings

import game_functions as gf
import pygame


def run_rocket_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Rocket Man")
    rocket = Rocket(ai_settings, screen)

    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


if __name__ == "__main__":
    run_rocket_game()

