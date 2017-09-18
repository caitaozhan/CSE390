__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


a = 1           # left bound
b = 3           # right bound
sample = 10000  # sample times

S = np.random.uniform(a, b, sample)

plt.figure('Cumulative Distribution')
plt.hist(S, bins=100, normed=True, cumulative=True)
plt.xlabel('x')
plt.ylabel('Pr[X<=x]')
plt.title('Uniform sample %d times between %.2f and %.2f' % (sample, a, b))
plt.grid()
plt.show()

