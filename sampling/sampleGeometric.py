__author__ = 'Caitao Zhan'
__email__  = 'caitao.zhan@stonybrook.edu'


import numpy as np
import matplotlib.pyplot as plt


n       = 100           # assume at most 100 trials (success for the first time within 100 trials)
p       = 0.07          # bernoulli's success probability
sample  = 5000          # sample times
counter = { i:0 for i in range(n+1) }
X       = np.arange(n+1)
P       = []

result = np.random.geometric(p, sample)

for i in result:
    if i <= n:          # neglect the outliers, whose value > n
        counter[i] += 1

for k, v in counter.items():
    P.append(float(v)/sample)

plt.figure('Probability Distribution')
plt.bar(X, P, 0.6)
x_axis  = np.arange(0, len(X), 5)
y_scale = max(P) / 10
y_axis  = np.arange(0, max(P)+y_scale, y_scale)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.xlabel('x')
plt.ylabel('Pr[X=x]')
plt.title('Geometric Sample %d times with n = %d, p = %f' % (sample, n, p))
plt.grid()

plt.show()
