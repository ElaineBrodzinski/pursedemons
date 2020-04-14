from typing import Tuple, Optional

from .surface import Surface

def set_mode(size: Tuple[int, int] = (0, 0)) -> Surface:
    """Initialize a window or screen for display
    """

def get_surface() -> Optional[Surface]:
    """Get a reference to the currently set display surface
    """

def set_caption(caption: str) -> None:
    """Set the current window caption
    """

def flip() -> None:
    """Update the full display Surface to the screen
    """
