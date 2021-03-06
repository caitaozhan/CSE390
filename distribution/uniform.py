__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


from distriBase import DistriBase
import numpy as np
import matplotlib.pyplot as plt


class Uniform(DistriBase):
    """Uniform distribution. 

    Agrs:
        a (float): left  bound
        b (float): right bound
    """

    def __init__(self, a, b):
        """Initialize uniform distribution with paramater a and b
           P(x) = 1/(b-a), a <= x < b
           P(x) = 0      , x < a or x >= b

        Args:
             a (float): left  bound
             b (float): right bound
        """
        DistriBase.__init__(self, 'Uniform')
        self.a = a
        self.b = b
        y_value = 1.0 / (b-a)
        self.X = np.linspace(a-1, b+1, num=1000, endpoint=False)
        x_scale = (b-a+2)/1000.0
        for i in self.X:
            if i < a:
                self.P.append(0)
                self.C.append(0)
            elif i > b:
                self.P.append(0)
                self.C.append(1)
            else:
                self.P.append(y_value)
                self.C.append((i-a) / (b-a))

    def __str__(self):
        return 'Name = %s, a = %f, b = %f' % (self.getName(), self.a, self.b)

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
    uniform = Uniform(1.1, 2.2)
    uniform.plot()
