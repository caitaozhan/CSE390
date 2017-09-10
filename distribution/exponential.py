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
        numSam = 2000      # number of samples
        x_scale = float(10-0)/numSam
        self.X = np.linspace(0, 10, num=numSam, endpoint=False)
        self.P = [0 for i in range(numSam)]
        self.C = [0 for i in range(numSam)]
        for i in range(numSam):
            self.P[i] = lamb * np.exp(-lamb * (i*x_scale))
        self.C[0] = self.P[0]*x_scale
        for i in range(1, numSam):
            self.C[i] = self.C[i-1] + self.P[i]*x_scale

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
        #plt.savefig('figures/exponential-pdf.png')

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()
        #plt.savefig('figures/exponential-cdf.png')

        plt.show()


if __name__ == '__main__':
    exponential = Exponential(1)
    exponential.plot()

