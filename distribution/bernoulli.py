__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt


class Bernoulli(DistriBase):
    """Bernolli Distribution.
    
    Attributes:
        p (float): success probability, range=(0, 1)
    """

    def __init__(self, p):
        """Initialize bernolli distribution with paramater p

        Args:
            p (float): success probability, range=(0, 1)
        """
        DistriBase.__init__(self, 'Bernoulli')
        self.p = p
        self.X = [0, 1]
        self.P = [1-p, p]
        self.C = [1-p, 1]

    def __str__(self):
        return 'Name = %s, p = %f' % (self.getName(), self.p)

    def plot(self):
        plt.figure('Probability Distribution')
        plt.bar(self.X, self.P, 0.6)
        x_axis = np.arange(len(self.X))
        y_axis = np.arange(0, 1.1, 0.1)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(str(self))
        #plt.savefig('figures/bernoulli-pdf.png')

        plt.figure('Cumulative Distribution')
        plt.bar(self.X, self.C, 0.6)
        x_axis = np.arange(len(self.X))
        y_axis = np.arange(0, 1.1, 0.1)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        #plt.savefig('figures/bernoulli-cdf.png')

        plt.show()


if __name__ == '__main__':
    bernoulli = Bernoulli(0.3)
    bernoulli.plot()
