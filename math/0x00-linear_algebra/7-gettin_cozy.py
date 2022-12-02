#!/usr/bin/env python3
"""define a function to use in the main file"""


def cat_matrices2D(mat1, mat2, axis=0):
  """verify de axis of the matrix to concatenate them"""
  if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return cat_arrays(mat1, mat2)
  elif axis == 1 and len(mat1) == len(mat2):
      return list(map(lambda arr1, arr2: cat_arrays(arr1, arr2), mat1, mat2))
  else:
      return None

def cat_arrays(arr1, arr2):
    """concatenates two arrays"""
    return arr1 + arr2

def matrix_shape(matrix):
    """function that returns the shape of a matrix"""
    shape = []
    while type(matrix) is list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]
    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)
    print(mat4)
    print(mat5)
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)
    print(mat4)
    print(mat5)