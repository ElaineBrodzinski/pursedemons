from typing import Tuple, Optional, TypeVar

from .rect import Rect

SurfaceT = TypeVar('SurfaceT', bound='Surface')
class Surface:
    """pygame object for representing images
    """
    def __init__(self, size: Tuple[int, int]):
        ...
    def get_bounding_rect(self, min_alpha: float = 1) -> Rect:
        """find the smallest rect containing data
        """
    def convert_alpha(self: SurfaceT) -> SurfaceT:
        """change the pixel format of an image including per pixel alphas
        """
    def get_rect(self) -> Rect:
        """get the rectangular area of the Surface
        """
    def get_width(self) -> int:
        """get the width of the Surface
        """
    def get_height(self) -> int:
        """get the height of the Surface
        """
    def get_size(self) -> Tuple[int, int]:
        """get the dimensions of the Surface
        """
    def get_at(self, top_left: Tuple[int, int]) -> Color:
        """get the color value at a single pixel
        """
    def subsurface(self: SurfaceT, rect: Rect) -> SurfaceT:
        """create a new surface that references its parent
        """
    def blit(self, source: Surface, dest: Rect) -> Rect:
        """draw one image onto another
        """
    def fill(self, color: Tuple[int, int, int]):
        """fill Surface with a solid color
        """
        

class Color:
    """pygame object for color representations
    """

    # Gets or sets the red value of the Color.
    r: int
    # Gets or sets the green value of the Color.
    g: int
    # Gets or sets the blue value of the Color.
    b: int
    # Gets or sets the alpha value of the Color.
    a: int

