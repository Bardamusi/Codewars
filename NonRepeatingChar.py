"""
5 kyu - First non-repeating character

Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("")
or None -- see sample tests.

"""


def first_non_repeating_letter(string):
    """
    :param string: string with any types of elements
    :return: returns the first char that is not repeated anywhere in string,
    or "" if there is no such char
    """
    freq_dict = {}
    lower = string.lower()

    # Counts occurrences of each object
    for char in lower:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # Finds the first occurrence
    for char in string:
        if freq_dict[char.lower()] == 1:
            return char
    else:
        return ""


def first_non_repeating_letter2(string):
    """
    :param string: string with any types of elements
    :return: returns the first char that is not repeated anywhere in string,
    or "" if there is no such char
    I feel like this implementation is much slower, but want to check.
    """
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""


if __name__ == "__main__":
    print('Basic Tests')
    print('should handle simple tests')
    print(first_non_repeating_letter('a'), 'a')
    print(first_non_repeating_letter('stress'), 't')
    print(first_non_repeating_letter('moonmen'), 'e')

    print('should handle empty strings')
    print(first_non_repeating_letter(''), '')

    print('should handle all repeating strings')
    print(first_non_repeating_letter('abba'), '')
    print(first_non_repeating_letter('aa'), '')

    print('should handle odd characters')
    print(first_non_repeating_letter('~><#~><'), '#')
    print(first_non_repeating_letter('hello world, eh?'), 'w')

    print('should handle letter cases')
    print(first_non_repeating_letter('sTreSS'), 'T')
    print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')