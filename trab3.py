import scipy.stats as stats
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

#Maximizacao a posteriori
class MAP:
    self.parameters = []

    #X is a matrix of datas
    #y is a target or label
    def fit(self, X, y):
        # temp = list(y)
        temp = list(set(y))
        for j in temp:
            pos = [i for i in xrange(len(y)) if y[i] == j]
            clss = X[pos]
            for i in range(0, len(clss[0])):
                col =clss[:, i]
                maxloglikelihood(col)
            # e^classe / soma (e^classes)

    #returns parameters for each col
    def maxloglikelihood(self, col):
        def loglikelihood(theta):
            soma = 0
            for x in col:
                soma += stats.norm.logpdf(x, theta[0], theta[1])
            return -soma
        result = opt.fmin(func, [1000, 1000])
        self.parameters.append(result)

    #given a new observation, return the probability of coming from each different class
    def predict(self, X):
        iris = datasets.load_iris()
        data = iris.data
        target = iris.target

pos = [i for i in xrange(len(target)) if target[i] == 0]
cls1 = data[pos]
col1 =  cls1[:,0]
#plt.hist(col1)
#plt.show()

#verossim function


#optmize mean value and variance of the normal curve
result = opt.fmin(func, [1000, 1000])
print result