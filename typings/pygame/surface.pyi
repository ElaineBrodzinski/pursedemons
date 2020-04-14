from typing import Tuple, Optional

from .rect import Rect

class Surface:
    """pygame object for representing images
    """

    def convert_alpha(self) -> Surface:
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
    def get_at(self, top_left: Tuple[int, int]) -> Color:
        """get the color value at a single pixel
        """
    def subsurface(self, rect: Rect) -> Surface:
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

