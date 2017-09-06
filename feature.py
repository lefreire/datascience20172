import numpy as np
import math
import matplotlib.pyplot as plt
import csv
data = open("novafeature.csv", 'r')
reader = csv.reader(data)


aux = []
for linha in reader:
    aux = aux + linha

n = 0
new_aux = []
for i in range(1, len(aux)):
    b = aux[i].split(";")
    new_aux = new_aux + [int(b[1])]
    n += 1

# calculating mean value
Xn = np.mean(new_aux)

#calcutating variance value
sd = (np.var(new_aux))**(0.5)

# u = (n**(0.5))*(Xn - Mi0)/dp
# n: number of values
# Xn: mean value of the data given
# sd: standard deviation

Mi0 = 65

print "mean value = ", Xn
print "n = ", n
u =  (n**(0.5))*(Xn - Mi0)/sd
print u
