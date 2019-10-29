"""
4 kyu - Hamming Numbers

A *Hamming number* is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

Specifically:

    The first smallest Hamming number is 1 = 203050
    The second smallest Hamming number is 2 = 213050
    The third smallest Hamming number is 3 = 203150
    The fourth smallest Hamming number is 4 = 223050
    The fifth smallest Hamming number is 5 = 203051

The 20 smallest Hamming numbers are given in example test fixture.

Your code should be able to compute all of the smallest 5,000 (Clojure: 2000) Hamming numbers without timing out.
"""

from heapq import heappush, heappop
from itertools import islice


def hammingBrute(n):
    """
    :param n: We are looking for the n-th Hamming number
    :return: returns it
    Uses basically brute force approach and sorting.
    DANGER: by virtue of the way the ranges are used it there are mistakes beyond a certain (unknown) index.
    For example suppose the m-th smallest hamming number is 2^52, it wouldn't be in the list, but some other number is.
    So this will fail without throwing an error.
    """
    h = sorted(2 ** i * 3 ** j * 5 ** k for i in range(50) for j in range(50) for k in range(50))
    return h[n-1]

def h():
    """
    Generator for list of Hamming numbers using heap method and priority queue
    Computes 3x more numbers than necessary, but discards them quickly so memory usage is not too bad.
    :return: next Hamming number
    """

    heap = [1]
    while True:
        h = heappop(heap)
        while heap and h == heap[0]:
            heappop(heap)
        for m in [2, 3, 5]:
            heappush(heap, m * h)
        yield h


def hamming(n):
    """Returns the nth hamming number"""
    return list(islice(h(), n - 1, n)).pop()


if __name__ == "__main__":

    print (list(islice(h(), 20)))
    print(list(islice(h(), 1690, 1691)))
    # print(list(islice(h(), 999999, 1000000)) )
    n = 10000
    print(n)
    print("---------")
    print(hamming(n))
    print("---------")
    print(hammingBrute(n))
