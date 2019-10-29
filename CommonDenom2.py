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

import math
import functools

from functools import reduce
from fractions import gcd

import copy

def convertFractsFast(lst):
    def lcm(x, y):
      s = x*y
      while y: x, y = y, x%y
      return s//x
    blst=copy.deepcopy(lst)
    for i in range(1,len(lst)):
      lst[i][1]=lcm(lst[i-1][1],lst[i][1])
    for i in range(len(lst)):
      lst[i][1]=lst[len(lst)-1][1]
      lst[i][0]=lst[i][1]*blst[i][0]//blst[i][1]
    return lst


def convertFractsFast2(lst):
    lcm = lambda x, y: x*y//gcd(x, y)
    D = reduce(lcm, (d for _, d in lst))
    return [[n*D//d, D] for n, d in lst]


def convertFractsFast3(lst):
    """
    :param lst:
    :return:
    Doesn't run
    """
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num], list(lst)))


if __name__ == "__main__":

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