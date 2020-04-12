from typing import Tuple

from .surface import Surface
from .rect import Rect
class SysFont:
    def __init__(self, name: str, size: int): ...

    def render(self, text: str, color: Tuple[int, int, int]) -> Tuple[Surface, Rect]: ...

def get_default_font() -> str: ...
