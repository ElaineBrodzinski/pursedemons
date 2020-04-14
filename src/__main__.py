from glob import glob
import random
import math
import sys
from itertools import count

import pygame
import pygame.image
import pygame.display
import pygame.freetype
import pygame.image
import pygame.mouse
import pygame.time
from pygame import Surface, Rect

from . import sprite_sheet


def main():
    pygame.init()
    font = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 24)
    window = pygame.display.set_mode((256 * 4, 256))

    clock = pygame.time.Clock()
    fps = 60
    t = 0

    # # Set up the window we'll be drawing in
    pygame.display.set_caption("banksrupt")

    # # Load our sprite sheet.
    sprites = sprite_sheet.load("assets/sprites")

    # Load the player image we'll be displaying.
    player_image = sprites[
        random.choice(
            [name for name in sprites if ("Ursus" in name or "Horribilis" in name)]
        )
    ]

    # # Load the font we'll use for text.

    # Loop forever until we set running to False, when the user tries to exit.
    while True:
        t += 1

        # Wait until it's time for the next frame to be drawn.
        clock.tick(fps)

        # Loop over every input or event that has happened since the last frame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                print("Exiting because the user told us to.")
                return

        # Fill the background
        window.fill((0, 0, 0))

        # Draw background layers
        for n, sprite in enumerate(
            (sprites["Vague Stone Wallpaper"], sprites["Black Void"],)
        ):
            for x in range(
                -((t * (1 + n)) % (sprite.get_rect().width * 2)),
                256 * 6,
                sprite.get_rect().width,
            ):
                r = sprite.get_rect()
                r.center = (x, 128 + n * 128)
                window.blit(sprite, r)

        # Take the new frame we've drawn and display it.
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
