from typing import Tuple, overload

class Rect:
    x: int
    y: int
    w: int
    h: int

    centerx: int
    centery: int
    
    top: int
    left: int
    bottom: int
    right: int

    width: int
    height: int
    size: Tuple[int, int]

    topleft: Tuple[int, int]
    midtop: Tuple[int, int]
    topright: Tuple[int, int]
    midleft: Tuple[int, int]
    center: Tuple[int, int]
    midright: Tuple[int, int]
    bottomleft: Tuple[int, int]
    midbottom: Tuple[int, int]
    bottomright: Tuple[int, int]

    @overload
    def __init__(self, top_left: Tuple[int, int], width_height: Tuple[int, int]): ...

    @overload
    def __init__(self, top: int, left: int, width: int, height: int): ...
