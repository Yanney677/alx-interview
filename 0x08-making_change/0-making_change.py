#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    dups = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            dups[i] = min(dups[i], dups[i - coin] + 1)
    return dups[-1] if dups[-1] != float("inf") else -1
