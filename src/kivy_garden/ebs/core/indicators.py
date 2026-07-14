from kivy.graphics import Color, PushMatrix, Rotate, Triangle, PopMatrix
from kivy.uix.widget import Widget


class ChevronWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0
        with self.canvas:
            self.color = Color(0.8, 0.8, 0.8, 1)
            PushMatrix()
            self.rot = Rotate(angle=self.angle, origin=self.center)
            self.tri = Triangle()
            PopMatrix()
        self.bind(pos=self._update_triangle, size=self._update_triangle)

    def _update_triangle(self, *_):
        # Simple right-pointing triangle
        cx, cy = self.center
        s = min(self.width, self.height) * 0.4
        self.tri.points = [
            cx - s, cy + s,
            cx - s, cy - s,
            cx + s, cy
        ]
        self.rot.origin = self.center

    def set_angle(self, deg):
        self.angle = deg
        self.rot.angle = deg
