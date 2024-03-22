#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the minimum number of operations needed to
                        transform a given number `n` into 1.

    Parameters:
        n (int): The number to be transformed.

    Returns:
        int: The minimum number of operations needed to transform `n` into 1.
    """
    if n == 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
