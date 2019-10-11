"""
6 kyu - Unique In Order
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements
with the same value next to each other
and preserving the original order of elements.

"""


def unique_in_order(iterable):
    """
    :param iterable: sequence with basically any type of entries
    :return: list with all elements with same value next to each other removed,
            and original order maintained
    """
    res = []
    old_letter = None
    for letter in iterable:
        if letter != old_letter:
            old_letter = letter
            res.append(old_letter)

    return res

if __name__ == "__main__":
    print(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C','D', 'A', 'B'])
    print(unique_in_order('ABBCcAD') )
    print(unique_in_order([1, 2, 2,3, 3]))
    print(unique_in_order([]))
