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
        if data is None:
            # If lambtha is not a positive value or equals to 0
            if lambtha < 1:
                raise ValueError("lambtha must be a positive value")
            else:
                # save lambtha as a float
                self.lambtha = float(lambtha)
        else:
            # if data is given
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                # If data does not contain at least two data points
                raise ValueError("data must contain multiple values")
            else:
                # Calculate the lambtha of data
                lambtha = float(sum(data) / len(data))
                self.lambtha = lambtha

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
            x[int] is the time period
            Returns the PDF value for x
        If x is out of range, return 0
        """
        e = 2.7182818285
        lambtha = self.lambtha
        if x < 0:
            return 0
        pdf = lambtha * (e ** (-lambtha * x))
        return pdf

    def cdf(self, x):
        """
        nstance method def cdf(self, x):

        Calculates the value of the CDF for a given time period
            x[int] is the time period
            Returns the CDF value for x
        If x is out of range, return 0
        """
        e = 2.7182818285
        lambtha = self.lambtha
        cdf = 1 - (e ** (-lambtha * x))
        return cdf
