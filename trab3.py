import scipy
import scipy.stats as stats
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

#Maximizacao a posteriori
class MAP:
    def __init__(self):
        #stores a tuple of parameters for each class in order
        #for example, parameters[0] is a tuple [mi,sigma] for col 0 of class 0
        self.parameters = []
        #stores the part over total for each class in order 
        self.probs = []
        self.doneFit = False
        self.eachClasses = {}
        self.numberOfClasses = 0

    #X is a matrix of datas
    #y is a target or label
    def fit(self, X, y):
        # temp = list(y)
        temp = list(set(y))
        self.numberOfClasses = len(temp)
        for j in temp:
            self.eachClasses[j] = temp[j]
            pos = [i for i in xrange(len(y)) if y[i] == j]
            clss = X[pos]
            self.probs.append(float(len(clss))/len(y))
            for i in range(0, len(clss[0])):
                col =clss[:, i]
                # print len(col)
                self.maxloglikelihood(col)
        self.doneFit = True
        print "Probs", self.probs
        print "parameters", self.parameters

    #returns parameters for each col
    def maxloglikelihood(self, col):
        # def loglikelihood(theta):
        #     soma = 0
        #     for x in col:
        #         soma += stats.norm.logpdf(x, theta[0], theta[1])
        #     return -soma
        # result = opt.fmin(loglikelihood, [1000, 1000])
        
        self.parameters.append((np.mean(col), np.var(col)))

    #given a new observation, return the probability of coming from each different class
    def predict(self, X):
        if self.doneFit == False:
            print "fit not yet done"
            exit(0)
        result = []
        for i in xrange(len(X)):
            result.append(-1)
            previousSum = -99999999999
            for j in xrange(self.numberOfClasses):
                sumOfLogs = 0
                for k in xrange(len(X[i])):
                    # print X[i][k]
                    # try:
                    sumOfLogs += scipy.stats.norm.logpdf(X[i][k], self.parameters[(j*len(X[0]))+k][0], (self.parameters[(j*len(X[0]))+k][1]))
                        # print scipy.stats.norm.logpdf(X[i][k], self.parameters[j+k][0], (self.parameters[j+k][1]))
                    # except:
                    #     sumOfLogs -= 1000000
                sumOfLogs += np.log(self.probs[j])
                print sumOfLogs, ':',j
                if sumOfLogs > previousSum:
                    previousSum = sumOfLogs
                    result[i] = j
        return result

def main():
    maps = MAP()
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    maps.fit(X, y)
    results = maps.predict(X)
    print results, y

if __name__ == "__main__":
    main()