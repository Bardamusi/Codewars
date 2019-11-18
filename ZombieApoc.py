"""
4 kyu - Zombie Apocalypse: the Last Number Standing

Todo: smallest number doesn't work, need to take different approach
"""


def findSmallest(arr):
    """
    :param arr: sorted array
    :return: Smallest number that cannot be represented as sum of subset of arr
    # Returns the smallest number
    """
    res = 1  # Initialize result
    size = len(arr)

    # Traverse the array and increment
    # 'res' if arr[i] is smaller than
    # or equal to 'res'.
    for i in range(0, size):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res


if __name__ == "__main__":
    arr1 = [1, 3, 4, 5]

    print(findSmallest(arr1))

    arr2 = [1, 2, 6, 10, 11, 15]

    print(findSmallest(arr2))

    arr3 = [1, 1, 1, 1]

    print(findSmallest(arr3))

    arr4 = [1, 1, 3, 4]

    print(findSmallest(arr4))