__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


trial = 100                                # sample trial times
p     = 0.3                                # bernoulli's success probability
success = np.random.binomial(1, p, trial)  # When n=1, binomial = bernoulli 
counter = 0
for i in success:
    if i == 1:
        counter += 1

p2 = float(counter)/trial

X = [0, 1]
P = [1-p2, p2]

plt.figure('Probability Distribution')
plt.bar(X, P, 0.6)
x_axis = np.arange(len(X))
y_axis = np.arange(0, 1.1, 0.1)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.xlabel('x')
plt.ylabel('Pr[X=x]')
plt.title('Bernoulli Sample %d times with p = %f' % (trial, p))
plt.grid()

plt.show()