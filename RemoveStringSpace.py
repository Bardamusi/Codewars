"""
8 kyu - Remove String Spaces
Simple, remove the spaces from the string, then return the resultant string.
https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
"""


def no_space(x):
    """
    :param x: takes a string
    :return: returns string with spaces removed
    note can also use string.replace(x, y) 
    """
    l = x.split(" ")  # Splits the string to a list with space as a separator
    res = "".join(l)  # turns list into a string with "" between two elements form list
    return res


if __name__ == "__main__":
    print("Basic tests")
    print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
    print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
    print(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
    print(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
    print(no_space('8j aam'), '8jaam')