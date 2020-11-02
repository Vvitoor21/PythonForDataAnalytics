print('DE acordo com o site BBC : Os países com maior número de casos registrados são Estados Unidos (7.279.065), '
      'Índia (6.394.068), Brasil (4.847.092), Rússia (1.188.928), Colômbia (835.339), Peru (814.829), Espanha (778.607),'
      ' Argentina (765.002), México (748.315) e África do Sul (676.084).')
      
import matplotlib.pyplot as plt

casos =[7279065,6394068,4847092,1188928,835339,814829,778607,765002,748315,676084]
paises=['Estados Unidos','Índia','Brasil','Rússia','Colômbia','Peru','Espanha','Argentina','México','África do Sul']

plt.barh(paises,casos)
plt.barh(paises[2],casos[2],color='green')
plt.title('Casos de COVID-19 em gráfico de colunas horizontal')
plt.xlabel('Casos')
plt.ylabel('Países')
plt.show()

plt.bar(paises,casos)
plt.bar(paises[2],casos[2],color='green')
plt.title('Casos de COVID-19 em gráfico de colunas vertical')
plt.xlabel('Casos')
plt.ylabel('Países')
plt.show()

plt.title('Ápice de casos por mês nos três países mais atingidos')
casos = [6935,20000,55851,45323,14297,15321]
casos2 = [20125,42000,70851,58323,54297,90321]
casos3 = [8135,17000,45851,65323,97297,55321]
meses = ['maio' , 'junho' , 'julho', 'agosto' ,'setembro','outubro']
plt.plot(meses,casos,marker='o',label='Brasil',color='green')
plt.plot(meses,casos2,marker='o',label='EUA',color='red')
plt.plot(meses,casos3,marker='o',label='ÍNDIA',color='orange')
plt.legend()
plt.xlabel('últimos meses')
plt.ylabel('Ápice de casos')
plt.show()

plt.pie(casos,labels=paises)
plt.show()

e = [0,0,0.1,0,0,0,0,0,0,0]
plt.pie(casos,labels=paises,explode=e,shadow=True)
plt.title('Casos de COVID-19 em gráfico de pizza. Destaque para o Brasil')
plt.show()


