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
    if n <= 1:
        return 0

    min_operations = 0
    current_length = 1
    clipboard = 0

    while current_length != n:
        if n % current_length == 0:
            clipboard = current_length
            min_operations += 1
        current_length += clipboard
        min_operations += 1

    return min_operations
