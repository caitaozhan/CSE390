__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import random
import statistics
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
    print('Generate a sequence of twenty random integers.')
    sequence = randomSeq(50)
    print(sequence)
    
    print('Mean     = %f' % statistics.mean(sequence))
    print('Std dev  = %f' % statistics.stdev(sequence))
    print('Median   = %f' % statistics.median(sequence))
    print('Variance = %f' % statistics.variance(sequence))
    
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

