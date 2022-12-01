#!/usr/bin/env python3
"""define a function to use in the main file"""


def add_arrays(arr1, arr2):
    """verify if the 2 input arrays have the same length and
    sum the value 1 with the value 1 of the arrays, consequently with
    every other value and if the arrays haven't the same length
    will return None"""
    if len(arr1) == len(arr2):
        return [arr1[x] + arr2[x] for x in range(len(arr1))]
    return None
