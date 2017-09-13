__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt
from scipy import special


class Normal(DistriBase):
    """Normal distribution.

    Args:
        m (float): mean or expectation of the distribution
        v (float): variance, the square of standard deviation
    """

    def __init__(self, m, v):
        """Initialize normal distribution with paramater m and var
           P(x | m, v) = e^( -(x-m)^2 / 2*v ) / (sqrt(2*PI*v))

        Args:
            m (float): mean, or expectation of the distribution
            v (float): variance, or square of standard deviation
        """
        DistriBase.__init__(self, 'Normal')
        self.m = m
        self.v = v
        self.xLen = np.sqrt(v) * 8       # plot data between [m - 4*sqrt(v), m + 4*sqrt(v)]
        len = self.xLen / 2.0            # len = 4*sqrt(v)
        self.X = np.linspace(m-len, m+len, num=1000, endpoint=False)
        for i in self.X:
            self.P.append(np.exp( -(i-m)**2 / (2*v) ) / np.sqrt(2*np.pi*v) )
        for i in self.X:
            self.C.append( (1 + special.erf( (i-m) / (np.sqrt(v*2))) ) / 2 )

    def __str__(self):
        return 'Name = %s, mean = %f, variance = %f' % (self.getName(), self.m, self.v)

    def plotRange(self, m, len):
        """Slightly adjust the x-axis range to plot more 'beautifully'

        Args:
            m   (float): mean of the distribution
            len (float): len = 4*sqrt(v)
        """
        left  = int(m-len-1) if (m-len < 0) else int(m-len)
        right = int(m+len+1) if (m+len > 0) else int(m+len)
        return left, right

    def plot(self):
        len = self.xLen/2.0
        plt.figure('Probability Distribution')
        plt.plot(self.X, self.P)
        left, right = self.plotRange(self.m, len)
        x_axis = np.arange(left, right, 1)
        y_scale = max(self.P) / 10
        y_axis = np.arange(0, max(self.P)+y_scale, y_scale)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(str(self))
        plt.grid()

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        left, right = self.plotRange(self.m, len)
        x_axis = np.arange(left, right, 1)
        plt.xticks(x_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()

        plt.show()


if __name__ == '__main__':
    normal = Normal(-2, 4)
    normal.plot()
