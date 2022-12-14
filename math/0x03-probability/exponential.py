#!/usr/bin/env python3
"""
exponential distribution
"""


class Exponential:
    """define class"""
    def __init__(self, data=None, lambtha=1.):
        """
        class constructor
        """
        # if data is not given
        if data is None and isinstance(lambtha, (float, int)):
            # If lambtha is not a positive value or equals to 0
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            # save lambtha as a float
            self.lambtha = float(lambtha)
        elif data is not None:
            # if data is given
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                # If data does not contain at least two data points
                raise ValueError("data must contain multiple values")
            # Calculate the lambtha of data
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
            x[int] is the time period
            Returns the PDF value for x
        If x is out of range, return 0
        """
        e = 2.7182818285
        if x is None or x < 0:
            return 0
        return (self.lambtha * (
            e ** ((-1 * self.lambtha) * x)
        ))

    def cdf(self, x):
        """
        nstance method def cdf(self, x):

        Calculates the value of the CDF for a given time period
            x[int] is the time period
            Returns the CDF value for x
        If x is out of range, return 0
        """
        e = 2.7182818285
        if x is None or x < 0:
            return 0
        return (1 - (
            e ** ((-1 * self.lambtha) * x)
        ))
