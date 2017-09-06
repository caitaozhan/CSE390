__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import random
 

def uniform(x, a, b):
    """Generates a random uniform sequence, where each floating point number is between [a, b].
    
    Args:
        a (float): start-point value
        b (float): end-point value
        n (int)  : the number of random numbers to be generated
    
    Returns:
        list: A sequence of floating point numbers
    """
    sequence = []
    for i in range(x):
        sequence.append(random.uniform(a, b))
    return sequence



