from typing import Tuple

class Rect:
    width: int
    height: int
    center: Tuple[int, int]
    midleft: Tuple[int, int]
    
    def __init__(self, top_left: Tuple[int, int], width_height: Tuple[int, int]): ...
