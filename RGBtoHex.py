"""
5 kyu - RGB To Hex Conversion
The rgb() method is incomplete.
Complete the method so that passing in RGB decimal values will result
in a hexadecimal representation being returned.
The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range
should be rounded to the closest valid value.
"""


def allowed(x, low=0, high=255):
    """
    :param x: value you want to round to nearest allowed value
    :param low: if x is smaller than this, we want low to be returned
    :param high: if x is bigger than this, we want high to be returned
    :return: x in [low, high]
    the default values are for RGB coding
    """
    if x < low:
        return low
    elif x > high:
        return high
    else:
        return x


def rgb(r, g, b):
    """
    :param r: :param g: :param b: All should be decimal numbers
    :return: their allowed RGB hexadecimal value in upper case.
    Note that if you input an "illegal" decimal value
    it will be rounded to 0 or 255 depending on which is closer.

    Also note that it's unclear what happens if you would enter no decimal numbers
    """
    hex_r = "{0:0=2X}".format(allowed(r), 'X')  # Note the second argument in format seems unnecessary
    hex_g = "{0:0=2X}".format(allowed(g), 'X')
    hex_b = "{0:0=2X}".format(allowed(b), 'X')

    return "".join([hex_r, hex_g, hex_b])

    # return ("{:02X}" * 3).format(allowed(r), allowed(g), allowed(b))
    # return "{:02X}{:02X}{:02X}".format(allowed(r), allowed(g), allowed(b))
    pass