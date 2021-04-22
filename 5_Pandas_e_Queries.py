import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_csv('C:/Users/vitor/Desktop/Estudos/DataSet.csv'))
print(data)

print(data.query('Nome=="Vitor"'))

print(data.query('Peso > 60'))

print(data.query('Peso > 60 and Local == "São Paulo"'))

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print('Somando as colunas verticais')
print(np.sum(arr,axis=0))
print('Somando as linhas horizontais')
print(np.sum(arr,axis=1))

print(arr.mean()) # Calcula a média (Especificar Coluna)

