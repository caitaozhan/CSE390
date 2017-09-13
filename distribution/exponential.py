__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt


class Exponential(DistriBase):
    """Exponential distribution.

    Agrs:
        lamb (float): lambda, rate parameter
    """

    def __init__(self, lamb):
        """Initialize exponential distribution with paramater lamb
           P(x) = lamb * e^(-lamb*x) , x >= 0
           P(x) = 0                  , x <  0

        Args:
             lamb (float): lambda, rate parameter
        """
        DistriBase.__init__(self, 'Exponential')
        self.lamb = lamb
        self.X = np.linspace(0, 10, num=1000, endpoint=False)
        for i in self.X:
            self.P.append( lamb * np.exp(-lamb * i) )
        for i in self.X:
            self.C.append( 1 - np.exp(-lamb * i) )

    def __str__(self):
        return 'Name = %s, lambda = %f' % (self.getName(), self.lamb)

    def plot(self):
        plt.figure('Probability Distribution')
        plt.plot(self.X, self.P)
        y_scale = max(self.P) / 10
        y_axis = np.arange(0, max(self.P)+y_scale, y_scale)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(str(self))
        plt.grid()

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()

        plt.show()


if __name__ == '__main__':
    exponential = Exponential(1)
    exponential.plot()

