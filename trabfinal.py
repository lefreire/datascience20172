import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score

file = open("train_set.csv")

mylines = file.read().split('\n')

alist = []
for i in xrange(0, len(mylines)):
    element = mylines[i].split(";")
    for j in xrange(0, len(element)):
        # print mylines[i][j]
        if element[j] == 'NA':
            alist.append(j)
print set(alist)

X = []
y = []
signal = 1
for line in mylines:
    if signal == 1:
        signal = 0
        continue
    element = line.split(";")
    try:
        d = [float(x) for x in element[0:-1]]
    except:
        for i in range(0, len(element[0:-1])):
            if element[i] == 'NA':
                 element[i] = 0
        d = [float(x) for x in element[0:-1]]
    try:
        y.append(int(element[-1]))
    except:
        continue
    X.append(d)

X = np.array(X)
y = np.array(y)

kf = KFold(10, shuffle=True)
metrics = []

for train_index, test_index in kf.split(X):
    clf = LogisticRegression()
    print 'x = ',X[train_index]
    print 'y = ',y[train_index]
    clf.fit(X[train_index],y[train_index])
    y_pred = clf.predict_proba(X[test_index])
    auc = roc_auc_score(y[test_index], y_pred[:,1])
    metrics.append(auc)

#must find greater average auc
print(metrics)

probs = clf.predict_proba(X[test_index])[:,1]
probs.sort()
print (probs[::-1])