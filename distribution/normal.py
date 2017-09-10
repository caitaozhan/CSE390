__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt


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
        len = self.xLen / 2.0              # len = 4*sqrt(v)
        numSam = 1000                    # number of samples
        x_scale = float(self.xLen)/numSam
        self.X = np.linspace(m-len, m+len, num=numSam, endpoint=False)
        self.P = [0 for i in range(numSam)]
        self.C = [0 for i in range(numSam)]
        for i in range(numSam):
            self.P[i] = np.exp( -((m-len + i*x_scale)-m)**2 / (2*v) ) / np.sqrt(2*np.pi*v)
        self.C[0] = self.P[0]*x_scale
        for i in range(1, numSam):
            self.C[i] = self.C[i-1] + self.P[i]*x_scale

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
        #plt.savefig('figures/normal-pdf.png')

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        left, right = self.plotRange(self.m, len)
        x_axis = np.arange(left, right, 1)
        plt.xticks(x_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()
        #plt.savefig('figures/normal-cdf.png')

        plt.show()


if __name__ == '__main__':
    normal = Normal(-2, 4)
    normal.plot()


