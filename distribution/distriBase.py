__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


class DistriBase:
    """The base class for all distributions.
    
    Attributes:
        name (str): the name of the distribution
        X   (list): x-axis 
        P   (list): y-axis (Probability distribution)
        C   (list): y-axis (Cumulative  distribution)
    """
    def __init__(self, distriName):
        self.name = distriName
        self.X = []
        self.P = []
        self.C = []

    def setName(self, distriName):
        self.name = distriName

    def getName(self):
        return self.name

    def plot(self):
        """Plot probability distribution function and cumulative distribution function."""
        pass

if __name__ == '__main__':
    distriBase = DistriBase('caitao')
    print(distriBase.getName())


