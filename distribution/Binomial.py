__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
from scipy.special import comb
import numpy as np
import matplotlib.pyplot as plt


class Binomial(DistriBase):
    """Binomial Distribution. P(X=i) = (n choose i) * p^i * (1-p)^(n-i)

    Attributies:
        n   (int): the number independent experiences. When n=1, binomial = bernoulli.
        p (float): probability of success in one independent experience
    """

    def __init__(self, n, p):
        """Initialize binomial distribution with paramater n and p

        Args:
            n   (int): the number independent experiences. When n=1, binomial = bernoulli.
            p (float): probability of success in one independent experience
        """
        DistriBase.__init__(self, 'Binomial')
        self.n = n
        self.p = p
        self.X = np.arange(0,n)
        for i in range(n):
            self.P.append(comb(n,i) * (p**i) * ((1-p)**(n-i)) )  
        self.C.append(self.P[0])
        for i in range(1, n):
            self.C.append(self.C[i-1] + self.P[i])

    def __str__(self):
        return 'Name = %s, n = %d, p = %f' % (self.getName(), self.n, self.p)

    def plot(self):
        plt.figure('Probability Distribution')
        plt.bar(self.X, self.P, 0.8)
        x_axis = np.arange(len(self.X))
        y_axis = np.arange(0, max(self.P)+0.02, 0.02)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(str(self))

        plt.figure('Cumulative Distribution')
        plt.plot(self.X, self.C)
        x_axis = np.arange(len(self.X))
        y_axis = np.arange(0, 1.1, 0.1)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X<=x]')
        plt.title(str(self))
        plt.grid()

        plt.show()


if __name__ == '__main__':
    binomial = Binomial(20, 0.35)
    binomial.plot()

