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
