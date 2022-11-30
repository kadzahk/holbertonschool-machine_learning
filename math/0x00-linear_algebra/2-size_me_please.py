#!/usr/bin/env python3
"""define a function to use in the main file"""


def matrix_shape(matrix):
    """count the elements and the number of vectors in an array
    by traversing them with a for loop"""
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
