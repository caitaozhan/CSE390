__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt


class Geometric(DistriBase):
    """Geometric distribution. P(X=i) = (1-p)^(i-1) * p.
       P(X=5) is the probability of getting the 1st success in the 5th trial 

    Attributes:
        p (float): success probability, the same p as in bernolli
    """

    def __init__(self, p):
        """Initialize bernolli distribution with paramater p

        Args:
            p (float): success probability, range=(0, 1)
        """
        DistriBase.__init__(self, 'Geometric')
        n = 100              # assume at most 100 trials
        self.p = p
        self.X = np.arange(0, n+1)
        self.P.append(0)     # P(0) has no meanings
        for i in range(1, n+1):
            self.P.append( ((1-p)**(i-1)) * p)
        self.C.append(0)
        for i in range(1, n+1):
            self.C.append(self.C[i-1] + self.P[i])

    def __str__(self):
        return 'Name = %s, p = %f' % (self.getName(), self.p)

    def plot(self):
        plt.figure('Probability Distribution')
        plt.bar(self.X, self.P, 0.6)
        x_axis = np.arange(0, len(self.X), 5)
        y_scale = max(self.P) / 10
        y_axis = np.arange(0, max(self.P)+y_scale, y_scale)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(str(self))

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        x_axis = np.arange(0, len(self.X), 5)
        y_axis = np.arange(0, 1.1, 0.1)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()

        plt.show()


if __name__ == '__main__':
    geometric = Geometric(0.07)
    geometric.plot()