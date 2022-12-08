#!/usr/bin/env python3
"""
calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    calculates the derivative of a polynomial
    with a loop to derivate each element
    in the list
    """
    if poly and isinstance(poly, list) and all(
        isinstance(i, (int, float)) for i in poly):
        deripol = [poly[x] * x for x in range(1, len(poly))]
        if not len(deripol):
            return [0]
        return deripol
    return None
