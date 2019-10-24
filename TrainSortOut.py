"""
7 kyu - Sort Out The Men From Boys

Now that the competition gets tough it will Sort out the men from the boys .
Men are the Even numbers and Boys are the odd
Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .

"""


def men_from_boys(arr):
    """
    :param arr: list with numbers, no zeroes (or they will be considered even)
    :return: new list with all duplicates removed, all the even numbers ordered ascending,
    and then all uneven numbers descending
    """
    res = sorted(list(set(arr)))  # sets have only unique elements so this removes all duplicates
    men = [x for x in res if x % 2 == 0]
    boys = [x for x in res if x % 2 != 0]
    return men + boys[::-1]


def men_from_boys2(arr):
    """
    :param arr: list with numbers, no zeroes (or they will be considered even)
    :return: new list with all duplicates removed, all the even numbers ordered ascending,
    and then all uneven numbers descending
    """
    return sorted(set(arr), key=lambda n: (n % 2, n * (-1) ** (n % 2)))