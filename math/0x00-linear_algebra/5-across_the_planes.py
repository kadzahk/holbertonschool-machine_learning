#!/usr/bin/env python3
"""define a function to use in the main file"""


def add_matrices2D(mat1, mat2):
    """function that adds two matrices element-wise"""
    if len(mat1) == len(mat2):
        mat3 = list(map(lambda arr1, arr2: add_arrays(arr1, arr2), mat1, mat2))
        if None in mat3:
            return None
        return mat3
    return None


def add_arrays(arr1, arr2):
    """function that adds two arrays element-wise"""
    if len(arr1) == len(arr2):
        return [arr1[x] + arr2[x] for x in range(len(arr1))]
    return None


def matrix_shape(matrix):
    """function that returns the shape of a matrix"""
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
