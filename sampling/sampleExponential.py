__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


scale  = 1.0      # scale parameter, the inverse of rate parameter
sample = 10000    # sample times

S = np.random.exponential(scale, sample)
plt.figure('Cumulative Distribution')
plt.hist(S, bins=100, normed=True, cumulative=True)
plt.xlabel('x')
plt.ylabel('Pr[X<=x]')
plt.title('Exponential sample %d times with rate parameter = %.2f' % (sample, 1/scale))
plt.grid()
plt.show()
