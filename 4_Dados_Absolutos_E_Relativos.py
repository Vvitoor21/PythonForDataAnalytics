import pandas as pd

import numpy as np

dados = { 'emprego':['Administrador de banco de dados', 'Arquiteto', 'Programador'],
         'sao_paulo':[97350, 82080, 112840],
         'rio': [77140, 71540, 62310] }
print(dados)
dataset = pd.DataFrame(dados)
print(dataset)
dataset['sao_paulo'].sum()
dataset['rio'].sum()
print(dataset)

dataset['Porcentagem_sp'] = dataset['sao_paulo'] / dataset['sao_paulo'].sum() * 100

dataset['Porcentagem_rio']= dataset['rio'] / dataset['rio'].sum() * 100
print(dataset)

dataset['Porcentagem_rio']= dataset['rio'] / dataset['rio'].sum() * 100
list = ['Total',dataset['sao_paulo'].sum(), dataset['rio'].sum(), dataset['Porcentagem_sp'].sum() ,dataset['Porcentagem_rio'].sum()]
print(list)
dataset.loc[len(dataset)] = list
print(dataset)

boletim = {'notas1': [8, 5, 9, 8],
                        'notas2': [8, 4, 6, 4],
                        'materia': ['bio', 'mat', 'por', 'qui']
                        }
print(boletim)
a = pd.DataFrame(boletim)
print(a)

a['media'] = a['notas1'] + a['notas2'] // 20
print('BOLETIM DE MÉDIAS E MATÉRIAS')
print(a)

print(a)

a['Aprovado'] = a['media'] > 5
print(a)


