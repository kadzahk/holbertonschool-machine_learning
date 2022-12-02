#!/usr/bin/env python3
"""define a function to use in the main file"""


def mat_mul(mat1, mat2):
    """multiplication of matrices"""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum([mat1[x][y] * mat2[y][row] for y in range(len(mat2))])
            for row in range(len(mat2[0]))] for x in range(len(mat1))]
