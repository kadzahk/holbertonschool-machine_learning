#!/usr/bin/env python3
"""
Normal distribution
"""


class Normal:
    """define class"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """
        class constructor
        data [list] data to be used to estimate the distibution
        mean [float] the mean of the distribution
        stddev [float] the standard deviation of the distribution
        """
        # If data is not given
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                #  Use the given mean and stddev
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                # Calculate the mean and standard deviation of data
                mean = float(sum(data) / len(data))
                self.mean = mean
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                stddev = (summation / len(data)) ** (1 / 2)
                self.stddev = stddev

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
            x is the x-value
            Returns the z-score of x
        """
        mean = self.mean
        stddev = self.stddev
        z = (x - mean) / stddev
        return z

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score
            z is the z-score
            Returns the x-value of z
        """
        mean = self.mean
        stddev = self.stddev
        x = (z * stddev) + mean
        return x

    def pdf(self, x):
        """
        cCalculates the value of the PDF for a given x-value
            x is the x-value
            Returns the PDF value for x
        """
        # mean = self.mean
        stddev = self.stddev
        e = 2.7182818285
        pi = 3.1415926536
        power = -0.5 * (self.z_score(x) ** 2)
        coeficiente = 1 / (stddev * ((2 * pi) ** (1 / 2)))
        pdf = coeficiente * (e ** power)
        return pdf

    def cdf(self, x):
        """
        calculates the value of the CDF for a given x-value
        parameters:
            x: x-value
        return:
            the CDF value for x
        """
        mean = self.mean
        stddev = self.stddev
        pi = 3.1415926536
        value = (x - mean) / (stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + erf)
        return cdf
