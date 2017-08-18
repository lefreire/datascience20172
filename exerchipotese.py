import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#slide copy
# data = np.random.poisson(3,20)
# print data

# print np.mean(data)

# x = ( (np.mean(data) - 3)*len(data)**(1.0/2.0) ) / (3**(1.0/2.0))
# print x

# pvalue = 1 - stats.norm.cdf(x)
# print pvalue

# print pvalue < 0.025

#exercise
tam = 200
rejeitou = 0
taxa = []
total = 0

for i in xrange(10000):
    amostra = np.random.poisson(3,tam)
    media = np.mean(amostra)
    x = ( (media - 3)*len(amostra)**(1.0/2.0) )
    x = x/(3**(1.0/2.0))
    if x > 0:
        pvalue = 1 - stats.norm.cdf(x)
    else:
        pvalue = stats.norm.cdf(x)

    if pvalue < 0.025:
        rejeitou += 1
    taxa.append(rejeitou/float(i+1))
    

plt.plot(taxa)
plt.show()