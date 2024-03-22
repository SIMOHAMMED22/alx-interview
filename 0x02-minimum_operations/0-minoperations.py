#!/usr/bin/python3
"""task0"""


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
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
