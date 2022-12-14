#!/usr/bin/env python3
"""
Poisson distribution
"""


class Poisson:
    """define class"""
    def __init__(self, data=None, lambtha=1.):
        """
        class constructor
        data [list] data to estimate the distribution
        lambtha [float] expected number of occurances on a given time
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

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of “successes”

        k[int] is the number of “successes”
        """
        e = 2.7182818285
        lambtha = self.lambtha
        facto_numb = 1
        if type(k) is not int:
            # If k is not an integer, convert it to an integer
            k = int(k)
        if k < 0:
            # If k is out of range, return 0
            return 0
        for x in range(k):
            facto_numb *= (x + 1)
        pmf = ((lambtha ** k) * (e ** -lambtha)) / facto_numb
        # Returns the PMF value for k
        return pmf

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of “successes”

        k[int] is the number of “successes”
        """
        cdf = 0
        if type(k) is not int:
            # If k is not an integer, convert it to an integer
            k = int(k)
        if k < 0:
            # If k is out of range, return 0
            return 0
        for x in range(k + 1):
            cdf += self.pmf(x)
        # Returns the CDF value for k
        return cdf
