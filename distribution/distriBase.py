__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


class DistriBase:
    """The base class for all distributions.
    
    Attributes:
        name (str): the name of the distribution
        X   (list): the value of x-axis
        Y   (list): the value of y-axis
    """
    def __init__(self, distriName):
        self.name = distriName
        self.X = []      # x-axis
        self.Y = []      # y-axis (value is probability)

    def setName(self, distriName):
        self.name = distriName

    def getName(self):
        return self.name

    def plotPDF(self):
        """Plot the probability distribution function."""
        pass 

    def plotCDF(self):
        """Plot the cumulative distribution function."""
        pass


if __name__ == '__main__':
    distriBase = DistriBase('caitao')
    print(distriBase.getName())

