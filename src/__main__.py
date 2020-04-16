from glob import glob
import random
import math
import sys
import typing
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


class Game:
    def __init__(self):
        pygame.init()

        self._surface = pygame.display.set_mode((256 * 4, 256))
        self._clock = pygame.time.Clock()
        self._fps = 4
        self._sprites = sprite_sheet.load("assets/sprites")
        self._backgrounds = []

        pygame.display.set_caption("banksrupt")

    def run(self) -> typing.NoReturn:

        while True:
            self._clock.tick(self._fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    pygame.quit()
                    sys.exit()
                    return

            self._surface.fill((150, 50, 100))

            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Wood Tile"].tile_on(self._surface)
            self._sprites["Stone Block"].tile_on(self._surface, interval=(16, 16))

            pygame.display.flip()


def main():
    Game().run()


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
