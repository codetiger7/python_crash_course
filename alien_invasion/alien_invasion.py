from settings import Settings
from ship import Ship

import game_functions as gf
import pygame


def run_game():
    # Initialize game, settings and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Star the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()

        # redraw and make visible on screen
        gf.update_screen(ai_settings, screen, ship)


run_game()