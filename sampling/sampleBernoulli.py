__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


p       = 0.3                                # bernoulli's success probability
sample  = 100                                # sample times
result  = np.random.binomial(1, p, sample)   # When n=1, binomial = bernoulli 
counter = 0
for i in result:
    if i == 1:
        counter += 1

p2 = float(counter)/sample

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
plt.title('Bernoulli Sample %d times with p = %f' % (sample, p))
plt.grid()

plt.show()