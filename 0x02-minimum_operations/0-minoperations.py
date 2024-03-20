#!/usr/bin/python3

"""Method that determines the number of minmum operations
    given n characters
"""


def minOperations(n):
    """
        A function that calculates the  number of operations
        needed to give a result of exactly n H characters.

        args: n: Number of characters to be displayed
        return: number of min operations
    """

    if n <= 1:
        return 0

    # Initialize the result
    min_ops = 0
    factors = 2

    # Start from 2 and find prime factors of n
    while factors <= n:
        if n % factors == 0:
            min_ops += factors
            n = n // factors
        else:
            factors += 1

    return min_ops
