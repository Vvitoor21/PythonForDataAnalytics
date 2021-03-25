import numpy as np
import matplotlib.pyplot as plt

rol = np.array([94, 63, 21, 17, 30, 37, 144, 18, 73, 111, 120, 135, 92, 47, 20, 138, 98, 81, 33, 74, 89,
       30, 37, 125, 54, 123, 4, 66, 125, 24, 14, 70, 93, 113, 86, 84, 115, 69, 143, 45, 102, 151,
       23, 108, 133, 74, 76, 115, 79, 93 ])
rol.sort()
print(rol)

tamanho_rol = len(rol)
print(f'TAMANHO DO ROL: {tamanho_rol}\n')


amplitude_amostal = rol.max() - rol.min()
print(f'AMPLITUDE AMOSTRAL: {amplitude_amostal}\n')

numero_de_classes = 1 + 3.3 * np.log10(tamanho_rol)
numero_de_classes = round(numero_de_classes)
print(f'NUMERO DE CLASSES: {numero_de_classes}\n')

numero_de_intervalo = amplitude_amostal // numero_de_classes
print(f'NUMERO DE INTERVALOS(STEPS) : {numero_de_intervalo}\n')

intervalos = np.arange(rol.min(), rol.max()+ 2 , step = numero_de_intervalo )
print(f'INTERVALOS : {intervalos}\n')

intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7 = 0, 0, 0, 0, 0, 0, 0
for i in range(tamanho_rol):   #VERIFICANDO UM POR UM DOS VALORES NO ARRAY
    if rol[i] >= intervalos[0] and rol[i] < intervalos[1]: #VERIFICANDO QTD NESSA CONDIÇÃO
        intervalo1 += 1
    elif rol[i] >= intervalos[1] and rol[i] < intervalos[2]:
        intervalo2 += 1
    elif rol[i] >= intervalos[2] and rol[i] < intervalos[3]:
        intervalo3 += 1
    elif rol[i] >= intervalos[3] and rol[i] < intervalos[4]:
        intervalo4 += 1
    elif rol[i] >= intervalos[4] and rol[i] < intervalos[5]:
        intervalo5 += 1
    elif rol[i] >= intervalos[5] and rol[i] < intervalos[6]:
        intervalo6 += 1
    elif rol[i] >= intervalos[6] and rol[i] < intervalos[7]:
        intervalo7 += 1
lista_de_frequencia = [intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7]
print(f'LISTA DE FREQUENCIAS : {lista_de_frequencia}')

lista_classes= []
for n in range(len(lista_de_frequencia)):
    lista_classes.append(str(intervalos[n])+'--'+str(intervalos[n+1]))

print(lista_classes)
plt.bar(lista_classes,lista_de_frequencia)
plt.xlabel('CLASSES')
plt.ylabel('FREQUÊNCIAS')
plt.title('GRÁFICO DE DISTRIBUIÇÃO DE FREQUÊNCIAS')
plt.show()

#--------------------------------------------- CODIGO REVISADO E COMENTADO ----------------------------------------------------

import numpy as np

import matplotlib.pyplot as plt

rol = np.array([94, 63, 21, 17, 30, 37, 144, 18, 73, 111, 120, 135, 92, 47, 20, 138, 98, 81, 33, 74, 89,
       30, 37, 125, 54, 123, 4, 66, 125, 24, 14, 70, 93, 113, 86, 84, 115, 69, 143, 45, 102, 151,
       23, 108, 133, 74, 76, 115, 79, 93 ])

print('ROL É O CONJUNTO DE DADOS DE UMA FORMA ORDENADA: CRESCENTE OU DECRESCENTE\n')
rol.sort()
print(rol)

print('\nCALCULANDO O TAMANHO DO ROL')
tamanho_rol = len(rol)
print(f'TAMANHO DO ROL: {tamanho_rol}\n')

print('CALCULANDO A AMPLITUDE AMOSTRAL: VALOR FINAL - VALOR INICIAL')
amplitude_amostal = rol.max() - rol.min()
print(f'AMPLITUDE AMOSTRAL: {amplitude_amostal}\n')


print('CALCULANDO O NUMERO DE CLASSES. CLASSES SÃO OS DIFERENTES INTERVALOS DENTRO DA TABELA DE DISTRIBUICAO DE FREQUENCIAS')
print('FORMULA : 1 + 3.3 * np.log10(tamanho do rol)')
numero_de_classes = 1 + 3.3 * np.log10(tamanho_rol)
numero_de_classes = round(numero_de_classes)
print(f'NUMERO DE CLASSES: {numero_de_classes}\n')


print('CALCULANDO O NUMERO DE INTERVALOS DAS CLASSES: RESULTADO DA AMPLITUDE AMOSTRAL // NUMERO DE CLASSES')
numero_de_intervalo = amplitude_amostal // numero_de_classes
print(f'NUMERO DE INTERVALOS (STEPS) : {numero_de_intervalo}\n')

print('O ALCANCE VAI DO VALOR MINIMO DO ROL ATE O MAXIMO, EFUTUANDO DIVISOES A CADA 21 RESULTADOS')
intervalos = np.arange(rol.min(), rol.max()+ 2 , step = numero_de_intervalo )
print(f'INTERVALOS : {intervalos}\n')

intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7 = 0, 0, 0, 0, 0, 0, 0

for i in range(tamanho_rol):   #VERIFICANDO UM POR UM DOS VALORES NO ARRAY
    if rol[i] >= intervalos[0] and rol[i] < intervalos[1]: #VERIFICANDO QTD NESSA CONDIÇÃO
        intervalo1 += 1
    elif rol[i] >= intervalos[1] and rol[i] < intervalos[2]:
        intervalo2 += 1
    elif rol[i] >= intervalos[2] and rol[i] < intervalos[3]:
        intervalo3 += 1
    elif rol[i] >= intervalos[3] and rol[i] < intervalos[4]:
        intervalo4 += 1
    elif rol[i] >= intervalos[4] and rol[i] < intervalos[5]:
        intervalo5 += 1
    elif rol[i] >= intervalos[5] and rol[i] < intervalos[6]:
        intervalo6 += 1
    elif rol[i] >= intervalos[6] and rol[i] < intervalos[7]:
        intervalo7 += 1

print('ASSIM OBTEMOS AS LISTA DE FREQUENCIAS')
lista_de_fre = [intervalo1, intervalo2, intervalo3, intervalo4, intervalo5, intervalo6, intervalo7]
print(f'LISTA DE FREQUENCIAS :\n{lista_de_fre}\n')

print('AGORA A LISTA DE CLASSES')
lista_class = []
for n in range(len(lista_de_fre)):
    lista_class.append(str(intervalos[n])+'--'+str(intervalos[n+1]))

print(lista_class)

plt.bar(lista_class,lista_de_fre)
plt.xlabel('CLASSES')
plt.ylabel('FREQUÊNCIAS')
plt.title('GRÁFICO DE DISTRIBUIÇÃO DE FREQUÊNCIAS')
plt.show()
