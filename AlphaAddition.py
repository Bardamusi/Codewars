"""
7 kyu - Alphabetical Addition
"""


def add_letters(*letters):
    vala = ord("a")
    helper = vala - 1
    sumer = sum(ord(c) - helper for c in letters) - 1
    res = sumer % 26 + vala
    return chr(res)


if __name__ == "__main__":
    print(add_letters("a", "b", "b"))