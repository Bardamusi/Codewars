"""
5 kyu - Greed is Good
Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.
"""


def score_single(roll):
    """
    :param roll: value of singe dice throw (ex: 1 or 2 or 5)
    :return: value of such a throw
    """
    score_dict = {}
    score_dict[1] = 100
    score_dict[5] = 50

    try:
        return score_dict[roll]
    except KeyError:
        return 0


def score_tripple(roll):
    """
    :param roll: value of triple  dice throw (ex: 6,6,6 or 2,2,2)
    :return: value of such a throw
    """
    score_dict = {}
    score_dict[1] = 1000
    score_dict[6] = 600
    score_dict[5] = 500
    score_dict[4] = 400
    score_dict[3] = 300
    score_dict[2] = 200

    try:
        return score_dict[roll]
    except KeyError:
        return 0


def score(dice):
    """
    :param dice: list with dice throws (in principle 5 but it works for any number)
    :return: score of throw, dependent on the 2 scoring functions for throws
    """
    freq_dict = {}
    for roll in dice:
        freq_dict[roll] = freq_dict.get(roll, 0) + 1

    result = 0
    for val in freq_dict:
        while freq_dict.get(val, 0) > 0:
            if freq_dict.get(val) >= 3:
                result += score_tripple(val)
                freq_dict[val] -= 3
            else:
                result += freq_dict.get(val) * score_single(val)
                freq_dict[val] = 0

    return result


if __name__ == "__main__":
    print(score([2, 3, 4, 6, 2]), 0)
    print(score([4, 4, 4, 3, 3]), 400)
    print(score([2, 4, 4, 5, 4]), 450)