from typing import Any, Mapping, Dict
import os.path
import json

import pygame
import pygame.image
from pygame import Surface, Rect


def trim_preserving_center(surface: Surface) -> Surface:
    width = surface.get_width()
    height = surface.get_height()

    trim_x = 0
    while trim_x < width // 2:
        for y in range(height):
            if not (
                surface.get_at((trim_x, y)).a == 0
                and surface.get_at((width - trim_x - 1, y)).a == 0
            ):

                break
        else:
            trim_x += 1
            continue
        break

    trim_y = 0
    while trim_y < height // 2:
        for x in range(width):
            if not (
                surface.get_at((x, trim_y)).a == 0
                and surface.get_at((x, height - trim_y - 1)).a == 0
            ):
                break
        else:
            trim_y += 1
            continue
        break

    if trim_x or trim_y:
        surface = surface.subsurface(
            (trim_x, trim_y), (width - trim_x * 2, height - trim_y * 2)
        )

    return surface


class SpriteSheet(Mapping[str, Surface]):
    _path: str
    _meta: Dict[str, Surface]
    _image: Surface
    _sprites: Dict[str, Surface]

    def __init__(self, path: str):
        self._path = path
        self._meta = json.load(open(self._path + ".json"))
        self._image = pygame.image.load(self._path + ".png").convert_alpha()

        self._sprites = {}

        for (name, data) in self._meta["frames"].items():
            meta = data["frame"]
            sprite = trim_preserving_center(
                self._image.subsurface(
                    Rect((meta["x"], meta["y"]), (meta["w"], meta["h"]),)
                )
            )
            self._sprites[name] = sprite

    def __getitem__(self, key: str) -> Surface:
        for potential_key in (key, f"{key} 0", f"{key} 1"):
            if potential_key in self._sprites:
                return self._sprites[potential_key]
        return self._sprites[key]

    def __iter__(self):
        return iter(self._sprites)

    def __len__(self):
        return len(self._sprites)


def load(path: str) -> SpriteSheet:
    return SpriteSheet(path)
