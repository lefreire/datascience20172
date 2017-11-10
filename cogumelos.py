import numpy as np
f = open("mushrooms.csv")
header = f.readline()
data = []
target = []

for line in f:
    line = line.replace('\n', '')
    data.append(line.split(',')[1:])
    target.append(line[0])

data = np.array(data)

for col in range(len(data.T)):
    opcoes = list(set(data.T[col]))
    nova_lista = []
    for linha in range(len(data)):
        lista = list(np.zeros(len(opcoes)))
        p = opcoes.index(data.T[col][linha])
        lista[p] = 1
        nova_lista.append(lista)
    try:
        data_new = np.concatenate((data_new, (np.array(nova_lista))), axis=1)
    except:
        data_new = np.array(nova_lista) 
    print(data_new.shape)

