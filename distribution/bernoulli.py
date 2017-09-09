__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt

class Bernoulli(DistriBase):
    """Bernolli Distribution.
    
    Attributes:
        p (float): the paramater of bernoulli distribution.
    """
    def __init__(self, distriName, p):
        """Initialize bernolli distribution with paramater p

        Args:
            distriName (str): distribution's name
            p (float)       : distribution's paramater, range (0, 1)
        """
        DistriBase.__init__(self, distriName)
        self.p = p
        self.X = [0, 1]
        self.Y = [1-p, p]

    def print(self):
        print('Name = ' + self.getName())
        print('P = %f' % self.p)

        
    def plotPDF(self):
        plt.bar(self.X, self.Y, 0.4)
        x_axis = np.arange(len(self.X))
        y_axis = np.arange(0, 1.1, 0.1)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('x')
        plt.ylabel('Pr[X=x]')
        plt.title(self.name)
        plt.grid()
        plt.show()
        

if __name__ == '__main__':
    bernoulli = Bernoulli('Bernoulli', 0.3)
    bernoulli.print()
    bernoulli.plotPDF()
