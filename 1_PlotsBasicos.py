import matplotlib.pyplot as plt

a = [2018,2019,2020,2021,2022,2023]
b = [2,5,6,4,7,8]
c = [5,4,6,3,2,8]

plt.plot(a,b,label = 'Fevereiro',marker = '.')
plt.plot(a,c,label = 'Janeiro',marker = '.')

plt.legend()
plt.show()
plt.pie(a,c)
plt.show()

import numpy as np

a = [ 1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = [1, 3, 5, 7, 9]
plt.plot(a, b, 'r', label='Linha Vermelha ' ,marker='o')
plt.plot(a,c,'b',label='Linha Azul', marker='o')
plt.title('Gráfico')
plt.legend()
plt.show()

anos = np.array([2017, 2018, 2019,2019 ,2020])
salarios = np.array([850,700,1600,1800,2400])
plt.plot(anos,salarios,'g')
plt.title('Últimos salários')
plt.xlabel('Anos')
plt.ylabel('Salários')
plt.show()

anos = [2014,2015,2016,2017,2018,2019,2020]
p = np.array([10254,11254,12548,13645,14452,15254,17500])
j = np.array([5000,10254,12541,10548,12000,14587,11450])
c = np.array([ 6125,8540,10542,11254,10265,12547,14567 ])
r = np.array([5542,6782,8457,5256,9458,10452,11000])
C =  np.array([ 8125,8540,10542,11254,13265,15547,13567])
js = np.array([7254,8254,7548,9645,10452,11254,13500])

plt.plot(anos,p,'blue',label='Python',marker='o')
plt.plot(anos,j,'orange',label='Java')
plt.plot(anos,c,'green',label='C')
plt.plot(anos,js,'yellow',label='JavaScript')
plt.plot(anos,C,'red',label='C+')
plt.plot(anos,r,'cyan',label='R')
plt.title('Linguagens de programação mais usadas')
plt.legend()
plt.xlabel('ANOS')
plt.ylabel('USUÁRIO')
plt.show()

#Documentação para cores do gráfico: https://matplotlib.org/3.3.2/tutorials/colors/colors.html 
