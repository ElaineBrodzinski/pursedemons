from typing import Tuple, overload

class Rect:
    width: int
    height: int
    center: Tuple[int, int]
    midleft: Tuple[int, int]

    @overload
    def __init__(self, top_left: Tuple[int, int], width_height: Tuple[int, int]): ...

    @overload
    def __init__(self, top: int, left: int, width: int, height: int): ...
