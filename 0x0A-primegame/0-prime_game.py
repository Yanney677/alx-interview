#!/usr/bin/python3
"""
Defines a Prime game
"""


def is_prime(num):
    """
    Check if a number is prime.

    Args:
    - num (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(limit):
    """
    Generate a list of prime numbers up to a given limit.

    Args:
    - limit (int): The upper limit for generating prime numbers.

    Returns:
    - list of int: A list of prime numbers up to the given limit.
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    """
    Determine the winner of each round of the game.

    Args:
    - x (int): The number of rounds to play.
    - nums (list of int): An array of n for each round.

    Returns:
    - str or None: The name of the player who won the most rounds,
    or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        # Generates a list of prime numbers up to n
        primes = find_primes(n)
        current_player = 'Maria'

        # Simulate the game for the current round
        while primes:
            if current_player == 'Maria':
                next_move = min(primes)
                # Remove next_move and its multiples from the set
                primes = [p for p in primes if p % next_move != 0]
                current_player = 'Ben'
            else:
                next_move = min(primes)
                # Remove next_move and its multiples from the set
                primes = [p for p in primes if p % next_move != 0]
                current_player = 'Maria'
        # Update the current of wins for each player
        if current_player == 'Maria':
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner of the game
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
