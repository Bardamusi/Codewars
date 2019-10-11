def printer_error(s):
    """
    :param s: string with ONLY lower case letters from a-z
    :return: {}/{} where first is number of errors and second value total len of list
    """

    asc2_a = ord("a")
    asc2_m = ord("m")
    n = len(s)

    total_good = 0
    for letter in s:
        val = ord(letter)
        if val <= asc2_m and val >= asc2_a:
            total_good += 1

    errors = n - total_good
    l_to_print = [str(errors), "/", str(n)]
    return "".join(x for x in l_to_print)


from re import sub


def printer_error2(s):
    """
    :param s: string with ONLY lower case letters from a-z
    :return: {}/{} where first is number of errors and second value total len of list
    But Using regular expression
    """
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))