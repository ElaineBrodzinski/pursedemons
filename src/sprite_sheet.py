from typing import Any, Mapping, Dict
import os.path
import json

import pygame
import pygame.image
from pygame import Surface, Rect


class SpriteSheet(Mapping[str, Surface]):
    _path: str
    _meta: Dict[str, Dict[str, Any]]
    _image: Surface
    _sprites: Dict[str, Surface]

    def __init__(self, path: str):
        self._path = path
        self._meta = json.load(open(self._path + ".json"))
        self._image = pygame.image.load(self._path + ".png").convert_alpha()

        self._sprites = {}

        for (name, data) in self._meta["frames"].items():
            meta = data["frame"]
            sprite = self._image.subsurface(
                Rect((meta["x"], meta["y"]), (meta["w"], meta["h"]))
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
