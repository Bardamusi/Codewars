def XOR(x, y):
    """
    :param x: :param y: integers in decimal
    :return: XOR of binary values between x and y and same index, then converted to decimal
    So suppose binary x = 1010 (10) and binary y = 10110 (22) from left to right looking at digits
    0 XOR 0 -> 0, 1 XOR 1 -> 0, 0 XOR 1 -> 1, 1 XOR 0 -> 1, and one left over digit for y -> 1
    result would be 1 1 1 0 0 (Where first 1 comes from left-over digit). 11000 to decimal is 28

    Unit tested successfully (so far)
    """

    bin_x = bin(x)
    bin_y = bin(y)

    XOR = x ^ y

    return XOR


c = (1, 2)
[x for x in range(28827050410 * 35165045587)]
print(XOR(*c))

# print(XOR(28827050410, 35165045587))

"---------------------------------------"

def elder_ageWrong(m, n, l, t):
    """
    :param m:
    :param n:
    :param l:
    :param t:
    :return:
    Idea was that the XOR would result in magic triangle with same values on row
    (different indices but all the same values so 1,2,3,4,5 but at different places)
    """
    if n > m:
        m, n = n, m

    h = m - l - 1
    z = ((h + 1) * h) / 2

    total_magic_rectangle = n * z
    print(total_magic_rectangle)

    res = total_magic_rectangle % t

    print(res)
    return res

    pass