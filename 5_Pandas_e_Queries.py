import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_csv('C:/Users/vitor/Desktop/Estudos/DataSet.csv'))
print(data)

print(data.query('Nome=="Vitor"'))

print(data.query('Peso > 60'))

print(data.query('Peso > 60 and Local == "São Paulo"'))

