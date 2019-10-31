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


"---------------------------------------"


def largest_pow(x):
    t = 1
    while t < x:
        t <<= 1
    return t


def range_sum(l, r):
    return (l + r) * (r - l + 1) // 2


def elder_age(m, n, l, t):
    if m == 0 or n == 0:
        return 0
    if m > n:
        m, n = n, m
    lm, ln = largest_pow(m), largest_pow(n)
    if l > ln:
        return 0

    if lm == ln:
        return (range_sum(1, ln - l - 1) * (m + n - ln) + elder_age(ln - n, lm - m, l, t)) % t

    if lm < ln:
        lm = ln // 2
        tmp = range_sum(1, ln - l - 1) * m - (ln - n) * range_sum(max(0, lm - l), ln - l - 1)
        if l <= lm:
            tmp += (lm - l) * (lm - m) * (ln - n) + elder_age(lm - m, ln - n, 0, t)
        else:
            tmp += elder_age(lm - m, ln - n, l - lm, t)
        return tmp % t


if __name__ == "__main__":
    print(elder_age(8, 5, 1, 100), 5)
    print(elder_age(8, 8, 0, 100007), 224)
    print(elder_age(25, 31, 0, 100007), 11925)
    print(elder_age(5, 45, 3, 1000007), 4323)
    print(elder_age(31, 39, 7, 2345), 1586)
    print(elder_age(545, 435, 342, 1000007), 808451)
    # You need to run this test very quickly before attempting the actual tests :)
    print(elder_age(28827050410, 35165045587, 7109602, 13719506), 5456283);