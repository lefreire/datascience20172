import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score


file = open("creditcard.csv")
header = file.readline()

X = []
y = []
for line in file:
    line = line.split(",")
    y.append(int(line[-1][1]))
    d = [float(x) for x in line[1:-1]]
    X.append(d)
print (y.count(1)/float(len(y)))

X = np.array(X)
y = np.array(y)

kf = KFold(10, shuffle=True)
metrics = []

for train_index, test_index in kf.split(X):
    clf = LogisticRegression()
    clf.fit(X[train_index],y[train_index])
    y_pred = clf.predict_proba(X[test_index])
    auc = roc_auc_score(y[test_index], y_pred[:,1])
    metrics.append(auc)

print(metrics)

probs = clf.predict_proba(X[test_index])[:,1]
probs.sort()
print (probs[::-1])
