__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


mu = 0          # mean
sigma = 1       # standard deviation
sample = 10000  # sample times

S = np.random.normal(mu, sigma, sample)
plt.figure('Cumulative Distribution')
plt.hist(S, bins=100, normed=True, cumulative=True)
plt.xlabel('x')
plt.ylabel('Pr[X<=x]')
plt.title('Normal sample %d times with mu = %.2f and sigma = %.2f' % (sample, mu, sigma))
plt.grid()
plt.show()

