"""
6 kyu - The Supermarket Queue

There is a queue for the self-checkout tills at the supermarket.
Your task is write a function to calculate the total time required
for all the customers to check out!

input

    customers: an array of positive integers representing the queue.
    Each integer represents a customer, and its value is the amount of time
    they require to check out.
    n: a positive integer, the number of checkout tills.

output

The function should return an integer, the total time required.

https://www.codewars.com/kata/the-supermarket-queue/train/python
"""


def queue_time(customers, n):
    """
    :param customers: list with ints that give time needed
    :param n: number of tills
    :return: total time to process entire queue as int
    Messy first attempt
    """
    size = len(customers)
    if size <= n:
        try:
            return max(customers)
        except ValueError:
            return 0

    at_till = customers[:n]
    left_over = customers[n:]

    total_time = 0
    while len(at_till) > 0:
        time_to_first_done = min(at_till)
        total_time += time_to_first_done

        at_till = [x - time_to_first_done for x in at_till]
        number_empty_tills = at_till.count(0)
        at_till = [x for x in at_till if x != 0]

        at_till += left_over[:number_empty_tills]
        left_over = left_over[number_empty_tills:]

    return total_time


def queue_time2(customers, n):
    """
    :param customers: list with ints that give time needed
    :param n: number of tills
    :return: total time to process entire queue as int
    note that time complexity is len(customers)
    """
    tills = [0] * n

    # Trick here is that we count how long each till is busy
    # By using the fact that the next customer in line will go to the till
    # which is done the earliest (in min(tills) time) at
    # till x, with x = tills.index(time_till_free)
    for time in customers:
        time_till_free = min(tills)
        index_free = tills.index(time_till_free)
        tills[index_free] += time

    return max(tills)
