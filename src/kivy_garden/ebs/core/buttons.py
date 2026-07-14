

from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import RoundedRectangle
from .image import BleedImage
from .colors import ColorBoxLayout


class BleedImageButton(ButtonBehavior, BleedImage):
    pass


class RoundedBleedImageButton(BleedImageButton):
    _bgelement = RoundedRectangle

    def __init__(self, radius=None, **kwargs):
        super(RoundedBleedImageButton, self).__init__(
            bgparams={'radius': radius}, **kwargs
        )

class ClickableBox(ButtonBehavior, ColorBoxLayout):
    """A BoxLayout that behaves like a button (clickable area)."""
    pass
