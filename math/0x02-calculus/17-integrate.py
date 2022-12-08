#!/usr/bin/env python3
"""
calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    funtion to calculate the integral of a list
    polymonial
    """
    if poly and isinstance(poly, list) and (
            isinstance(C, int) or isinstance(C, float)) and all(
            isinstance(x, (int, float)) for x in poly):
        if poly == [0]:
            return[C]
        arr = [float(C)] + [poly[y] / (y + 1) for y in range(0, len(poly))]
        return [float(x) if not x.is_integer() else int(x) for x in arr]
    return None
