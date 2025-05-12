#!/usr/bin/python3
"""Module for calculating the minimum operations to reach n H characters."""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to get exactly n H
    characters using only Copy All and Paste operations.

    Args:
        n (int): Target number of characters.

    Returns:
        int: Minimum number of operations or 0 if n < 2.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
