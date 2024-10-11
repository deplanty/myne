from ..color_bis import *


def test_color_rgb():
    """Test the color as float"""

    # Test initialization
    rgb = ColorRGB(0.0, 0.5, 1.0)
    assert rgb.r == 0.0
    assert rgb.g == 0.5
    assert rgb.b == 1.0
    assert rgb.rgb == (0.0, 0.5, 1.0)

    # Test setter
    rgb.r = 0.5
    rgb.g = 1.0
    rgb.b = 0.0
    assert rgb.r == 0.5
    assert rgb.g == 1.0
    assert rgb.b == 0.0

    # Test conversion to RGB hexadecimal
    assert rgb.hex == "#80ff00"

    # Test conversion to RGB int
    rgb_int = rgb.to_rgb_int()
    assert rgb_int.r == 128
    assert rgb_int.g == 255
    assert rgb_int.b == 0

    # Test conversion to HSV
    hsv = rgb.to_hsv()
    assert hsv.h == 0.25
    assert hsv.s == 1.0
    assert hsv.v == 1.0


def test_color_rgb_int_1():
    """Test the color as 1 byte integer"""

    # Test initialization
    rgb_int = ColorRGBInt(0, 128, 255, 1)
    assert rgb_int.r == 0
    assert rgb_int.g == 128
    assert rgb_int.b == 255
    assert rgb_int.rgb == (0, 128, 255)

    # Test setter
    rgb_int.r = 128
    rgb_int.g = 255
    rgb_int.b = 0
    assert rgb_int.r == 128
    assert rgb_int.g == 255
    assert rgb_int.b == 0

    # Test conversion to RGB hexadecimal
    assert rgb_int.hex == "#80ff00"

    # Test conversion to RGB float
    rgb = rgb_int.to_rgb()
    assert round(rgb.r, 3) == 0.502
    assert round(rgb.g, 3) == 1.000
    assert round(rgb.b, 3) == 0.000

    # Test conversion to HSV
    hsv = rgb_int.to_hsv()
    assert round(hsv.h, 3) == 0.250
    assert round(hsv.s, 3) == 1.000
    assert round(hsv.v, 3) == 1.000


def test_color_hsv():
    """Test the color as HSV float"""

    # Test initialization
    hsv = ColorHSV(0.1, 0.5, 0.9)
    assert round(hsv.h, 3) == 0.100
    assert round(hsv.s, 3) == 0.500
    assert round(hsv.v, 3) == 0.900
    assert hsv.hsv == (0.1, 0.5, 0.9)

    # Test setter
    hsv.h = 0.25
    hsv.s = 1.0
    hsv.v = 0.9
    assert round(hsv.h, 3) == 0.250
    assert round(hsv.s, 3) == 1.000
    assert round(hsv.v, 3) == 0.900

    hsv.v = 1.0

    # Test conversion to RGB hexadecimal
    assert hsv.hex == "#80ff00"

    # Test conversion to RGB float
    rgb = hsv.to_rgb()
    assert round(rgb.r, 3) == 0.500
    assert round(rgb.g, 3) == 1.000
    assert round(rgb.b, 3) == 0.000

    # Test conversion to RGB int
    rgb_int = hsv.to_rgb_int()
    assert rgb_int.r == 128
    assert rgb_int.g == 255
    assert rgb_int.b == 0


if __name__ == "__main__":
    test_color_rgb()
    test_color_rgb_int_1()
    test_color_hsv()
