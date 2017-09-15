import scipy.stats as stats
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
data = iris.data
target = iris.target

pos = [i for i in xrange(len(target)) if target[i] == 0]
cls1 = data[pos]
col1 =  cls1[:,0]
#plt.hist(col1)
#plt.show()

#verossim function
def func(theta):
    soma = 0
    for x in col1:
        soma += stats.norm.logpdf(x, theta[0], theta[1])
    return -soma

#optmize mean value and variance of the normal curve
result = opt.fmin(func, [1000, 1000])
print result