import matplotlib.pyplot as plt
import numpy as np

p = np.array([10254,11254,12548,13645,14452,15254,17500])
j = np.array([5000,10254,12541,10548,12000,14587,11450])
c = np.array([ 6125,8540,10542,11254,10265,12547,14567 ])
r = np.array([5542,6782,8457,5256,9458,10452,11000])
C =  np.array([ 8125,8540,10542,11254,13265,15547,13567])
js = np.array([7254,8254,7548,9645,10452,11254,13500])
width = 0.10

anos = np.arange(2014,2021)


plt.style.use('fivethirtyeight')
plt.style.use('dark_background')


plt.bar(anos + width,p,width = width,color ='blue',label='Python')
plt.bar(anos,j,width = width,color ='orange',label='Java')
plt.bar(anos - width,c,width = width,color ='green',label='C')
plt.bar(anos + (width*2),js,width = width,color ='yellow',label='JavaScript')
plt.bar(anos + (width*3),r,width = width,color ='cyan',label='R')
plt.bar(anos + (width*4),C,width = width,color ='red',label='C+')
plt.title('Linguagens de programação mais usadas')
plt.legend()
plt.xlabel('ANOS')
plt.ylabel('USUÁRIO')
plt.show()
