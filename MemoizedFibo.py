"""
5 kyu - Memoized Fibonacci
For this particular Kata we want to implement the memoization solution.
This will be cool because it will let us keep using the tree recursion algorithm
while still keeping it sufficiently optimized to get an answer very rapidly.

https://www.codewars.com/kata/memoized-fibonacci/train/python

Note - this is still a slow implementation of Fibonacci
(unless you want to get all values between 0 and n)
"""


fibo_dict = {}
fibo_dict[0] = 0
fibo_dict[1] = 1


def fibonacci(n):
    if n in fibo_dict:
        return fibo_dict[n]

    fibo_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibo_dict[n]


def memoized(f):
    """
    :param f: input is function below @memoized
    :return: the value for function below @memoized evaluated at the parameters
    If you call fibonacci2(y) args  will be equal to y (at first pass ?)
    """
    cache = {}

    def wrapped(*args):
        v = cache.get(args)
        if v is None:
            v = cache[args] = f(*args)
        return v
    return wrapped

@memoized
def fibonacci2(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    #print(fibo_dict)
    #print(fibonacci(500))
    print(fibonacci2(20))