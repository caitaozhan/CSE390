__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


"""Description:
A simple program that generates x random numbers and computes mean, 
std dev, median, variance, etc. Maybe also sort and plot the points.
"""


import random
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
# Caveat! Python-3.6.0(64-bit) crashes with numpy-1.13, thus causing matplotlib unable to import
# If you are using 3.6.0, then upgrade to the latest Python.


def randomSeq(x, n=10):
    """Generate a random integer sequence

    Args:
        x (int): the number of integers to be generated
        n (int): the value of integers is between [0,n]
    Return:
        list: a sequence of integers
    """
    sequence = []
    for i in range(x):
        sequence.append(int(random.random()*n))
    return sequence


if __name__ == '__main__':
    print('Generate a sequence of fifty random integers.')
    sequence = randomSeq(50)
    print(sequence)
    
    print('Mean     = %f' % stat.mean(sequence))
    print('Std dev  = %f' % stat.stdev(sequence))
    print('Median   = %f' % stat.median(sequence))
    print('Variance = %f' % stat.variance(sequence))
    
    plt.plot(sequence, 'ro')
    x_axis = np.arange(len(sequence))
    minValue = min(sequence)
    maxValue = max(sequence)
    y_axis = np.arange(minValue, maxValue+1)
    plt.xticks(x_axis)
    plt.yticks(y_axis)
    plt.grid()
    plt.show()

    print('The sequence is now sorted!')
    sequence.sort()
    print(sequence)

