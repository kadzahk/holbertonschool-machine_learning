#!/usr/bin/env python3
"""
sumation function for a power 2 int
"""


def summation_i_squared(n):
    """
    series sumation formula for power of 2
    """
    if isinstance(n, int) and n > 0:
        return int((n * ((2 * n) + 1)) / 6)
