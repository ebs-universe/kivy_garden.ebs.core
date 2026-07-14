from colorthief import ColorThief
from PIL import Image as PILImage

from kivy.uix.image import Image

from .colors import BackgroundColorMixin

from kivy.graphics.opengl import glGetIntegerv
from kivy.graphics.opengl import GL_MAX_TEXTURE_SIZE


_image_max_size = None


def _get_max_texture_size():
    """
    Lazily query the maximum OpenGL texture size.

    This must not happen at module import time because there may not yet
    be an active OpenGL context.
    """
    global _image_max_size

    if _image_max_size is None:
        _image_max_size = glGetIntegerv(GL_MAX_TEXTURE_SIZE)[0]

    return _image_max_size


class SizeProofImage(Image):
    def __init__(self, **kwargs):
        source = kwargs.get('source', None)
        if source:
            PILImage.MAX_IMAGE_PIXELS = None
            im = PILImage.open(source)
            size = im.size

            image_max_size = _get_max_texture_size()

            sf = max([float(s) / image_max_size for s in size])

            if sf > 1:
                target = [int(s / sf) for s in size]
                print(
                    "Resizing image {1} to {2} {0}".format(
                        source, size, target
                    )
                )
                im = im.resize(target, PILImage.ANTIALIAS)
                im.save(source)

            im.close()
            del im

        Image.__init__(self, **kwargs)


StandardImage = SizeProofImage


class BleedImage(BackgroundColorMixin, StandardImage):
    def __init__(self, **kwargs):
        bgcolor = kwargs.pop('bgcolor', 'auto')
        bgparams = kwargs.pop('bgparams', {})

        StandardImage.__init__(self, **kwargs)
        BackgroundColorMixin.__init__(self, **bgparams)

        if bgcolor == 'auto':
            self._autoset_bg_color()
            self.bind(source=self._autoset_bg_color)
        else:
            self.bgcolor = bgcolor

    def _autoset_bg_color(self, *_):
        color = ColorThief(self.source).get_color(5)
        self.bgcolor = [x / 255 for x in color] + [1.0]