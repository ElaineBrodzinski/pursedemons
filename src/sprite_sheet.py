from typing import Any, Mapping, Dict, Tuple, Optional
import os.path
import json

import pygame
import pygame.image
from pygame import Surface, Rect


class Sprite(Surface):
    def trim(self) -> "Sprite":
        return self.subsurface(self.get_bounding_rect())

    def tile_on(
        self, target: Surface, *, interval: Optional[Tuple[int, int]] = None,
    ):
        tile_width, tile_height = self.get_size()
        target_width, target_height = target.get_size()

        interval_x, interval_y = interval if interval else (tile_width, tile_height)

        for x in range(0, target_width, interval_x):
            for y in range(0, target_height, interval_y):
                if __import__("random").random() < (x / target_width):
                    # print(
                    #     f"{target}.blit({self}, Rect({x}, {y}, {tile_width}, {tile_height}))"
                    # )
                    target.blit(self, Rect(x, y, tile_width, tile_height))


class SpriteSheet(Mapping[str, Sprite]):
    _path: str
    _meta: Dict[str, Dict[str, Any]]
    _image: Sprite
    _sprites: Dict[str, Sprite]

    def __init__(self, path: str):
        self._path = path
        self._meta = json.load(open(self._path + ".json"))
        loaded = pygame.image.load(self._path + ".png").convert_alpha()
        self._image = Sprite(loaded.get_size())
        self._image.blit(loaded, loaded.get_rect())

        self._sprites = {}

        for (name, data) in self._meta["frames"].items():
            frame = data["frame"]
            sprite = self._image.subsurface(
                Rect(frame["x"], frame["y"], frame["w"], frame["h"],)
            )
            print(self._image, name, sprite)
            self._sprites[name] = sprite

    def __getitem__(self, key: str) -> Sprite:
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
