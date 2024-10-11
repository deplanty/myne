#
# Links between the classes
# =========================
#
# Color RGB:
#     from_rgb_int -> calc
#     from_hex -> calc
#     from_hsv -> calc
#
# Color RGB Int:
#     from_rgb -> calc
#     from hex -> ColorRGB.from_hex
#     from_hsv -> ColorRGB.from_hsv
#
# Color HSV:
#     from_rgb -> calc
#     from_rgb_int -> ColorRGB.from_rgb_int
#     from hex -> ColorRGB.from_hex



class ColorRGB:
    def __init__(self, r:float=0.0, g:float=0.0, b:float=0.0):
        """0.0 <= rgba <= 1.0"""
        self._r = float(r)
        self._g = float(g)
        self._b = float(b)

    def __str__(self):
        def s(value:float):
            if round(value, 1) == value:
                return f"{value:.1f}"
            elif round(value, 2) == value:
                return f"{value:.2f}"
            else:
                return f"{value:.3f}"
        return f"ColorRGB({s(self._r)}, {s(self._g)}, {s(self._b)})"

    # Properties

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value:int):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value:int):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value:int):
        self._b = value

    @property
    def rgb(self):
        return self._r, self._g, self._b

    @property
    def hex(self) -> str:
        r, g, b = self.rgb
        r = round(255 * r)
        g = round(255 * g)
        b = round(255 * b)
        return f"#{r:02x}{g:02x}{b:02x}"

    # Method

    def to_rgb_int(self, n_bytes:int=1):
        return ColorRGBInt.from_rgb(self, n_bytes)

    def to_hsv(self):
        return ColorHSV.from_rgb(self)

    # Classmethods

    @classmethod
    def from_rgb_int(cls, rgb_int:"ColorRGBInt"):
        maxi = pow(2, 8 * rgb_int._n_bytes) - 1
        r = rgb_int.r / maxi
        g = rgb_int.g / maxi
        b = rgb_int.b / maxi
        return cls(r, g, b)

    @classmethod
    def from_hex(cls, hex:str):
        hex = hex.lstrip("#")
        r = int(hex[0:2], 16) / 255
        g = int(hex[2:4], 16) / 255
        b = int(hex[4:6], 16) / 255
        return cls(r, g, b)

    @classmethod
    def from_hsv(cls, hsv:"ColorHSV"):
        h, s, v = hsv.hsv

        h = h * 360
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c

        if h < 60:
            r_, g_, b_ = c, x, 0
        elif h < 120:
            r_, g_, b_ = x, c, 0
        elif h < 180:
            r_, g_, b_ = 0, c, x
        elif h < 240:
            r_, g_, b_ = 0, x, c
        elif h < 300:
            r_, g_, b_ = x, 0, c
        else:
            r_, g_, b_ = c, 0, x

        r = r_ + m
        g = g_ + m
        b = b_ + m

        return cls(r, g, b)


class ColorRGBInt:
    def __init__(self, r:int=0, g:int=0, b:int=0, n_bytes=1):
        """0 <= rgb <= 255"""
        self._r = r
        self._g = g
        self._b = b

        if n_bytes > 1:
            raise ValueError("Multi-bytes color not implemeted yet")
        self._n_bytes = n_bytes

    def __str__(self):
        return f"ColorRGBInt({self._r:d}, {self._g:d}, {self._b:d})"

    # Properties

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value:int):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value:int):
        self._g = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value:int):
        self._b = value

    @property
    def rgb(self):
        return self._r, self._g, self._b

    @property
    def hex(self) -> str:
        return ColorRGB.from_rgb_int(self).hex

    # Methods

    def to_rgb(self):
        return ColorRGB.from_rgb_int(self)

    def to_hsv(self):
        return ColorHSV.from_rgb_int(self)

    # Classmethods

    @classmethod
    def from_rgb(cls, rgb:"ColorRGB", n_bytes:int=1):
        maxi = pow(2, 8 * n_bytes) - 1
        r = round(rgb.r * maxi)
        g = round(rgb.g * maxi)
        b = round(rgb.b * maxi)

        return cls(r, g, b, n_bytes)

    @classmethod
    def from_hex(cls, hex:str, n_bytes:int=1):
        rgb = ColorRGB.from_hex(hex)
        return cls.from_rgb(rgb, n_bytes)

    @classmethod
    def from_hsv(cls, hsv:"ColorHSV", n_bytes:int=1):
        rgb = ColorRGB.from_hsv(hsv)
        return cls.from_rgb(rgb)


class ColorHSV:
    def __init__(self, h:float=0.0, s:float=0.0, v:float=0.0):
        """0.0 <= hsva <= 1.0"""
        self._h = h
        self._s = s
        self._v = v

    def __str__(self):
        return f"ColorHSV({self._h}, {self._s}, {self._v})"

    # Properties

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value:float):
        self._h = value

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value:float):
        self._s = value

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value:float):
        self._v = value

    @property
    def hsv(self):
        return self._h, self._s, self._v

    @property
    def hex(self):
        return ColorRGB.from_hsv(self).hex

    # Methods

    def to_rgb(self):
        return ColorRGB.from_hsv(self)

    def to_rgb_int(self, n_bytes:int=1):
        return ColorRGBInt.from_hsv(self, n_bytes)

    # Classmethods

    @classmethod
    def from_rgb(cls, rgb:"ColorRGB"):
        r, g, b = rgb.rgb
        Cmax = max(r, g, b)
        Cmin = min(r, g, b)
        dC = Cmax - Cmin

        # Compute h for hue
        if dC == 0:
            h = 0
        elif Cmax == r:
            h = 60 * (((g - b) / dC) % 6)
        elif Cmax == g:
            h = 60 * ((b - r) / dC + 2)
        elif Cmax == b:
            h = 60 * ((r - g) / dC + 4)
        else:
            h = 0
        h /= 360

        # Compute s for saturation
        if Cmax == 0:
            s = 0
        else:
            s = dC / Cmax

        # Compute v for value
        v = Cmax

        return cls(h, s, v)

    @classmethod
    def from_rgb_int(cls, rgb_int:"ColorRGBInt"):
        # Convert to RGB float then to HSV
        rgb = ColorRGB.from_rgb_int(rgb_int)
        return cls.from_rgb(rgb)

    @classmethod
    def from_hex(cls, hex:str):
        rgb = ColorRGB.from_hex(hex)
        return cls.from_rgb(rgb)
