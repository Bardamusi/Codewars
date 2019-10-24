"""
6 kyu Reversing a Process
Suppose we know the process (A) by which a string s has been coded to a string r.

The aim of the kata is to decode r to get back the original string s.
Explanation of the known process (A):

    data: a string s composed of lowercase letters from a to z and a positive integer num

    we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...

    if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26
    then find ch the corresponding character of f(x)

    Accumulate all these ch in a string r.

    concatenate num and r and return the result.

    Todo : start
    https://www.codewars.com/kata/reversing-a-process/train/python
"""

def decode(r):
    # your code
    pass