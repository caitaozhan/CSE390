__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


n       = 5             # the number independent experiences
p       = 0.35          # bernoulli's success probability
sample  = 1000          # sample times
counter = { i:0 for i in range(n+1) }
X       = np.arange(n+1)
P       = []

result = np.random.binomial(n, p, sample)

for i in result:
    counter[i] += 1

for k, v in counter.items():
    P.append(float(v)/sample)

plt.figure('Probability Distribution')
plt.bar(X, P, 0.8)
x_axis = np.arange(len(X))
y_axis = np.arange(0, max(P)+0.02, 0.02)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.xlabel('x')
plt.ylabel('Pr[X=x]')
plt.title('Binomial Sample %d times with n = %d, p = %f' % (sample, n, p))
plt.grid()

plt.show()
