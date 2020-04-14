from typing import Tuple

from pygame.locals import *

from . import (
    surface, image, key, event, display, mouse, time, rect, freetype, transform, locals
)

Surface = surface.Surface
Rect = rect.Rect

def init() -> Tuple[int, int]:
    """initialize all imported pygame modules
    """

def quit() -> None:
    """uninitialize all pygame modules
    """
