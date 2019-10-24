"""
5 kyu - Simple fraction to mixed number converter
Task

Given a string representing a simple fraction x/y, your function must return a string representing the
corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction.
There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero)
and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero,
return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).
"""


def gcd(a, b):
    """
    :param a: integer
    :param b: integer
    :return: greatest common divisor using Euclid's Algorithm
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mixed_fraction(s):
    """
    :param s: string with two integers x and y represented as "x/y", x might be negative and/or y might be as well
    :return: return mixed fraction with nice lay-out
    """
    numer, denom = s.split("/")
    numer, denom = int(numer), int(denom)

    sign = "" if numer / denom >= 0 else "-"

    numer, denom = abs(numer), abs(denom)

    a = numer // denom
    helper = numer % denom

    gr_common_div = gcd(helper, denom)
    new_numer = helper // gr_common_div
    new_denom = denom // gr_common_div

    whole = "" if a == 0 and new_numer != 0 else str(a)
    fraction = "" if new_numer == 0 else str(new_numer) + str("/") + str(new_denom)
    helper2 = "" if fraction == "" or whole =="" else " "

    return "".join([sign, whole, helper2, fraction])


if __name__ == "__main__":
    print(mixed_fraction('42/9'), '4 2/3')
    print(mixed_fraction('6/3'), '2')
    print(mixed_fraction('4/6'), '2/3')
    print(mixed_fraction('0/18891'), '0')
    print(mixed_fraction('-10/7'), '-1 3/7')
    print(mixed_fraction('-22/-7'), '3 1/7')

