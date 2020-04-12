from typing import Any, Mapping, Dict
import os.path
import json

import pygame
import pygame.image
from pygame import Surface, Rect


class SpriteLoader(Mapping[str, Surface]):
    _path: str
    _meta: Dict[str, Surface]
    _image: Surface
    _sprites: Dict[str, Surface]

    def __init__(self, path: str):
        self._path = path
        self._meta = json.load(open(self._path + ".json"))
        self._image = pygame.image.load(self._path + ".png").convert_alpha()

        self._sprites = {
            name: self._image.subsurface(
                Rect(
                    (metadata["frame"]["x"], metadata["frame"]["y"]),
                    (metadata["frame"]["w"], metadata["frame"]["h"]),
                )
            )
            for (name, metadata) in self._meta["frames"].items()
        }

    def __getitem__(self, key: str) -> Surface:
        return self._sprites[key]

    def __iter__(self):
        return iter(self._sprites)

    def __len__(self):
        return len(self._sprites)


def load(path: str) -> SpriteLoader:
    return SpriteLoader(path)
