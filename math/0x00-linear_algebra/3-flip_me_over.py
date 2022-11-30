#!/usr/bin/env python3
"""define a function to use in the main file"""


def matrix_transpose(matrix):
    """all the values in te position 1 of every vector are going to be in the vector 1
    consequently with all vectors depending on the position"""
    return [[matrix[y][x] for y in range(len(matrix))]
          for x in range(len(matrix[0]))]
