"""
5 kyu - Common Denominators

You will have a list of rationals in the form

[ [numer_1, denom_1] , ... [numer_n, denom_n] ]

where all numbers are positive ints.

You have to produce a result in the form

[ [N_1, D] ... [N_n, D] ]

in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
"""



def lcm(x, y):
    """
    :param x: positive int
    :param y: positive int
    :return: least common multiple using the gcd
    """
    return x * y / gcd(x, y)

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


def test_sol(lst_number):
    """
    :param lst_number: list of numbers
    :return: returns True if all numbers are integers, False otherwise
    """
    for number in lst_number:
        if number != int(number):
            return False

    return True


def convertFracts(lst):
    """
    :param lst: [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
    :return: list such that N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
    Brute force solution. -> we can clearly improve updating step for d
    """
    numer = [x[0] for x in lst]
    denom = [x[1] for x in lst]

    d = 1
    bigN = [(numer[i] / denom[i]) * d for i in range(len(lst))]

    while not test_sol(bigN):
        d += 1
        bigN = [(numer[i] / denom[i]) * d for i in range(len(lst))]

    sol = [ [int(bigN[i]), d] for i in range(len(lst))]

    return sol


def convertFractsFast(lst):
    """
    :param lst: lst: [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
    :return:  list such that N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

    """
    numer = [x[0] for x in lst]
    denom = [x[1] for x in lst]
    unique = sorted(list(set(denom)))

    d = 1
    for number in unique:
        # We need to test if the smallest unique lcm fits as D, and if it doesn't
        # We use that the next smallest possible D is the lcm of the lcm of the last d and the next smallest number
        # in unique
        d = lcm(d, number)
        bigN = [numer[i] * (d / denom[i]) for i in range(len(lst))]
        if test_sol(bigN):
            res = [[int(bigN[i]), int(d)] for i in range(len(lst))]
            return res

    return []


if __name__ == "__main__":
    a = 16.5
    if a == int(a):
        print("yay")
    else:
        print("booo")

    a = [[1, 2], [1, 3], [1, 4]]
    print(convertFractsFast(a))

    a2 = []
    print(convertFractsFast(a2))

    a3 = [[2, 7], [1, 3], [1, 12]]
    print(convertFractsFast(a3))

    a4 = [[8, 15], [7, 111], [4, 25]]
    print(convertFractsFast(a4))

    a5 = [[27115, 5262], [87546, 11111111], [43216, 255689]]
    print(convertFractsFast(a5))

    print("Test", int(27115 * (14949283383840498 // 5262)))
