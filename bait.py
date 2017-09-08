import numpy as np
import math
import matplotlib.pyplot as plt
import csv

#grupo I - amostra A
#grupo II - amostra B

#classe A - yes
#classe B - no


data_a = open("amostraA.csv", 'r')
data_b = open("amostraB.csv", 'r')

reader_a = csv.reader(data_a)
reader_b = csv.reader(data_b)

aux_a = []
for linha in reader_a:
    aux_a = aux_a + linha


aux_b = []
for linha in reader_b:
    aux_b = aux_b + linha

n = 0    
new_aux_a = []
for i in range(1, len(aux_a)):
    b = aux_a[i].split(";")
    new_aux_a = new_aux_a + [b[1]]
    n += 1

n = 0    
new_aux_b = []
for i in range(1, len(aux_b)):
    b = aux_b[i].split(";")
    new_aux_b = new_aux_b + [b[1]]
    n += 1


yes_a = 0
no_a = 0

for i in range(len(new_aux_a)):
    if new_aux_a[i] == 'yes':
        yes_a += 1
    else:
        no_a += 1

yes_b = 0
no_b = 0

for i in range(len(new_aux_b)):
    if new_aux_b[i] == 'yes':
        yes_b += 1
    else:
        no_b += 1

T = yes_a + yes_b + no_a+ no_b

print "yes a: ", yes_a
print "yes b: ", yes_b
print "no a: ", no_a
print "no b: ", no_b


grupo1_a = ((yes_a + yes_b) * (yes_a+no_a)) / T
grupo2_a =  ((yes_a + yes_b) * (yes_b + no_b))/T
grupo1_b = ((no_a + no_b) * (yes_a + no_a))/T
grupo2_b = ((no_a + no_b)* (yes_b + no_b))/T

print "grupo1_a: ", grupo1_a
print "grupo2_a: ", grupo2_a
print "grupo1_b: ", grupo1_b
print "grupo2_b: ", grupo2_b

chi_1_1 = ((yes_a - grupo1_a) ** 2)/grupo1_a
chi_1_2 = ((no_a - grupo1_b) ** 2)/grupo1_b
chi_2_1 = ((yes_b - grupo2_a) ** 2)/grupo2_a
chi_2_2 = ((no_b - grupo2_b) ** 2)/grupo2_b

print chi_1_1
print chi_1_2
print chi_2_1
print chi_2_2

soma = chi_1_1 + chi_1_2 + chi_2_1 + chi_2_2

print "qui quadrado: ", soma
