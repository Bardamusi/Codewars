"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

"""


def alphabet_position(text):
    """Takes as input a string (with an ord() value)
        and returns the index in the alphabet of all 26 letters
    """

    lower_text = text.lower()  # To avoid having to deal with capital and lower case

    position_list = []
    for element in lower_text:
        asc2 = ord(element) - 96  # Since a is 97
        if 0 < asc2 < 27:  # Only take the letters
            position_list.append(asc2)

    return " ".join(str(x) for x in position_list)


def alphabet_position2(text):
    """
    :param text: string
    :return: and returns the index in the alphabet of all 26 letter
    Special here is that I learned about isalpha() method on strings
    """
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())