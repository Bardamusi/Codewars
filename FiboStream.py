"""
5 kyu - Fibonacci Streaming
You're going to provide a needy programmer a utility method that generates an infinite sized,
sequential IntStream (in TypeScript Iterator<number>, in Python generator)
which contains all the numbers in a fibonacci sequence.

A fibonacci sequence starts with two 1s. Every element afterwards is the sum of the two previous elements.

"""


def all_fibonacci_numbers():
    """
    :return: Generator for Fibonacci numbers
    """
    # just used to initialize sequence, by yielding a and then using definition of fib(n) = fib(n-1) + fib(n-2)
    a = 1
    b = 0

    while True:
        yield a
        b = a+b
        yield b
        a = a+b


if __name__ == "__main__":
    number = 30
    f = all_fibonacci_numbers()
    for i in range(number):
        print("The " + str(i+1) + "th Fibonacci number: ", f.__next__())
