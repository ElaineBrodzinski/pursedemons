from . import (
    surface, image, key, event, display, mouse, time, rect, freetype, transform
)

Surface = surface.Surface
Rect = rect.Rect

def init(): ...

def quit(): ...

# Event constants
QUIT: str
MOUSEBUTTONDOWN: str
MOUSEMOTION: str
KEYDOWN: str
KEYUP: str

# Keycode constants
K_ESCAPE: int
K_LEFT: int
K_RIGHT: int
K_UP: int
K_DOWN: int
K_a: int
K_d: int
K_s: int
K_w: int
