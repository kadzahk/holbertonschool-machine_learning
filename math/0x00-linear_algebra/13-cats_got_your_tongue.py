#!/usr/bin/env python3
"""define a function to use in the main file"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """function that concatenates two matrices
    with a specific axis"""
    return np.concatenate((mat1, mat2), axis)
