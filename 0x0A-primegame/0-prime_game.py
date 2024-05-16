#!/usr/bin/python3
"""Define the Prime Game
"""


def isWinner(i, nums):
    """The determination of the prime game"""
    if i < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    # Generate a list of prime number based on the max numbers in num
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False

    # count the no of pm less than n i nums
    for n in nums:
        count = sum(primes[2:n+1])
        ben_wins += count % 2 == 0
        maria_wins += count % 2 == 1

    if maria_wins == ben_wins:
        return None

    return 'Maria' if maria_wins > ben_wins else 'Ben'
