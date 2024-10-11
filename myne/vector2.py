import math


class Vector2:
    def __init__(self, x:float=0, y:float=0):
        self.x = x
        self.y = y

    # Magics

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __eq__(self, value):
        """Return self == value"""

        return self.x == value.x and self.y == value.y

    def __add__(self, value):
        """Return self + value"""

        v = Vector2()
        if isinstance(value, type(self)):
            v.x = self.x + value.x
            v.y = self.y + value.y
        else:
            v.x = self.x + value
            v.y = self.y + value

        return v

    def __mul__(self, value):
        """Return self * value"""

        v = Vector2()
        if isinstance(value, type(self)):
            v.x = self.x * value.x
            v.y = self.y * value.y
        else:
            v.x = self.x * value
            v.y = self.y * value
        return v

    def __rmul__(self, value):
        """Return value * self"""

        v = Vector2()
        if isinstance(value, type(self)):
            v.x = self.x * value.x
            v.y = self.y * value.y
        else:
            v.x = self.x * value
            v.y = self.y * value
        return v

    def __sub__(self, value):
        """Return self - value"""

        return self.__add__(value * -1)

    def __truediv__(self, value):
        """Return self / value"""

        v = Vector2()
        if isinstance(value, type(self)):
            v.x = self.x / value.x
            v.y = self.y / value.y
        else:
            v.x = self.x / value
            v.y = self.y / value
        return v

    def __floordiv__(self, value):
        """Return self // value"""

        v = Vector2()
        if isinstance(value, type(self)):
            v.x = self.x // value.x
            v.y = self.y // value.y
        else:
            v.x = self.x // value
            v.y = self.y // value
        return v

    def __abs__(self):
        """Return abs(self)"""
        return Vector2(abs(self.x), abs(self.y))

    # Property

    @property
    def xy(self):
        """Return the tuple (x, y)"""
        return self.x, self.y

    # Methods - Data manipulation

    def set(self, x:float, y:float):
        self.x = x
        self.y = y

    def zero(self):
        """Set the vector to (0, 0)"""

        self.x = 0
        self.y = 0

    # Methods - Calculation

    def dot(self, other):
        """Return the dot product"""
        return self.x * other.x + self.y * other.y

    def length(self):
        """Return the length"""
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def length_squared(self):
        """Return the squared length (faster than `length`)"""
        return pow(self.x, 2) + pow(self.y, 2)

    def distance_to(self, other) -> float:
        delta = self - other
        return delta.length()

    def distance_square_to(self, other) -> float:
        delta = self - other
        return delta.length_squared()

    def get_angle(self, other=None):
        """Return the angle between two vectors"""

        if other is None:
            other = Vector2(1, 0)

        dot = self.dot(other)
        norm = self.norm() * other.norm()

        if norm == 0:
            angle = 0
        else:
            # Round to avoid float estimation like 1.0000000000000002
            # Where acos is defined [-1, 1]
            angle = math.acos(round(dot / norm, 8))

        diff = other - self
        if diff.y < 0:
            return - angle
        else:
            return angle

    def is_parallel(self, other):
        return self.normalize() == other.normalize()

    # Methods - Export new vector

    def normalize(self):
        norm = self.norm()
        if norm == 0:
            return Vector2()
        else:
            return Vector2(self.x / norm, self.y / norm)

    def floor(self):
        """Return the floored vector"""
        return Vector2(int(self.x), int(self.y))

    def round(self):
        """Return the rounded vector"""
        return Vector2(round(self.x), round(self.y))

    def rotate(self, angle:float, origin=None):
        """
        Rotate a vector by angle rad.
        Can rotate around an origin.
        """

        if origin is None:
            origin = Vector2(0, 0)

        x = self.x - origin.x
        y = self.y - origin.y

        v = Vector2()
        v.x = math.cos(angle) * x - math.sin(angle) * y
        v.y = - (math.sin(angle) * x + math.cos(angle) * y)

        return v + origin

    def direction_to(self, other):
        direction = self - other
        return direction.normalize()

    def normal(self):
        return Vector2(-self.y, self.x).normalize()

    def bounce(self, surface):
        normal = surface.normal()
        surface = surface.normalize()
        return - self.dot(normal) * normal + self.dot(surface) * surface
