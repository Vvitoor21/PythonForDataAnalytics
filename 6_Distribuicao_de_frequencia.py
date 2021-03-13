import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
"""
print(np.array(np.random.randint(1,60,50)))

rol =np.array(np.random.randint(1,60,50))
rol.sort()

print(rol)

len = len(rol)

print(rol.min())

print(rol.max())

# i = numero de classe
i = 1 + 3.3 * np.log10(len)
i = round(i)

print(i)
"""
"""
rol =np.array([2,  3,  6 , 6 , 6 , 6,  7,  8,  9 ,11, 12, 12, 12, 14, 18, 19, 19, 19, 20, 20, 25, 26, 28, 31,
 36, 37, 37, 38, 38, 39, 40, 40, 41, 41, 43, 44, 44, 45, 46, 48, 49, 50, 52, 52, 53, 54, 56, 56,
 57, 57])


rol.sort()
print(rol)

max = rol.max()
min = rol.min()

aa = max - min
print(f'AMPLITUDE AMOSTRAL: {aa}')

len = len(rol)
print(f'TAMANHO DO ROL: {len}')

i = 1 + 3.3 * np.log10(len)
i = round(i)
print(f'NUMERO DE CLASSES: {i}')

amp = 55 / 7
amp = round(amp)
print(f'AMPLITUDE DO INTERVALO: {amp}')

intervalos = np.arange(rol.min(), rol.max() + 2, step = 8)
print(list(intervalos))

intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7 = 0, 0, 0, 0, 0, 0, 0

for i in range(len):
    if rol[i] >= intervalos[0] and rol[i] < intervalos[1]: # = Qtd de cada numero dentro dessa classe
        intervalo1 +=1
    elif rol[i] >= intervalos[1] and rol[i] < intervalos[2]:  # = Qtd de cada numero dentro dessa classe
        intervalo2 += 1
    elif rol[i] >= intervalos[2] and rol[i] < intervalos[3]:  # = Qtd de cada numero dentro dessa classe
        intervalo3 += 1
    elif rol[i] >= intervalos[3] and rol[i] < intervalos[4]:  # = Qtd de cada numero dentro dessa classe
        intervalo4 += 1
    elif rol[i] >= intervalos[4] and rol[i] < intervalos[5]:  # = Qtd de cada numero dentro dessa classe
        intervalo5 += 1
    elif rol[i] >= intervalos[5] and rol[i] < intervalos[6]:  # = Qtd de cada numero dentro dessa classe
        intervalo6 += 1
    elif rol[i] >= intervalos[6] and rol[i] < intervalos[7]:  # = Qtd de cada numero dentro dessa classe
        intervalo7 += 1

classes = [intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7]

print(classes)

"""
dados = np.array([160,165,167,164,160,166,160,161,150,152,173,160,155,
                  164,168,162,161,168,163,156,155,169,151,170,164,
                  155,152,163,160,155,157,156,158,158,161,154,161,156,172,153])
print(dados)
print('TAMANHO DO ROL')
n = len(dados)
print(n)

print('NUMERO DE CLASSES')
i = 1+ 3.3 * np.log10(n)
i = round(i)
i
print(i)

MIN = dados.min()
MAX = dados.max()
AA = MAX - MIN
print('AMPLITUDE AMOSTRAL')
print(AA)

print('AMPLITUDE DO INTERVALO')
Amp = AA / i
Amp = round(Amp)
print(Amp)

intervalo = np.arange(dados.min(), dados.max() +2 , step=4)
print('NUMEROS DO INTERVALO INTERVALO')
print(intervalo)

intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6 = 0, 0, 0, 0, 0, 0

for i in range(n):   #VERIFICANDO UM POR UM DOS VALORES NO ARRAY
    if dados[i] >= intervalo[0] and dados[i] < intervalo[1]: #VERIFICANDO QTD NESSA CONDIÇÃO
        intervalo1 += 1
    elif dados[i] >= intervalo[1] and dados[i] < intervalo[2]:
        intervalo2 += 1
    elif dados[i] >= intervalo[2] and dados[i] < intervalo[3]:
        intervalo3 += 1
    elif dados[i] >= intervalo[3] and dados[i] < intervalo[4]:
        intervalo4 += 1
    elif dados[i] >= intervalo[4] and dados[i] < intervalo[5]:
        intervalo5 += 1
    elif dados[i] >= intervalo[5] and dados[i] < intervalo[6]:
        intervalo6 += 1

classes = [intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6]

lista_classe = []
for n in range(len(classes)):  #Lendo quantos intervalos
    lista_classe.append(str(intervalo[n])+'--'+str(intervalo[n+1])) #pra cada intervalo

print(lista_classe)

plt.bar(lista_classe,classes)
plt.show()