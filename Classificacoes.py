#calda #presas #branquias #pata  / 0 = Peixe ; 1 = Cachorro  #Identificação de dados e classificações

peixe1 = [1,1,1,0]
peixe2 = [1,0,1,0]
peixe3 = [1,1,1,0]

cachorro1 = [0,1,0,0]
cachorro2 = [0,1,0,0]
cachorro3 = [0,0,0,0]

dados = [peixe1, peixe2, peixe3, cachorro1, cachorro2, cachorro3]
classes = [0,0,0,1,1,1]

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(dados, classes)

animal = [1,1,1,1]
model.predict([animal])

desconhecido1 = [1,1,0,1] # cachorro
desconhecido2  = [1,1,1,1] # peixe
desconhecido3 = [0,0,1,0] # peixe
teste = [desconhecido1, desconhecido2, desconhecido3]

previsao = model.predict(teste)
previsao

certo = [1, 0, 0]
previsao == certo

from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(certo, previsao)
print("Taxa de acerto %.2f "% (taxa_de_acerto * 100))

#2º Exemplo de calculo da acuracia----------------------------------------------------------------------------
from sklearn.svm import LinearSVC

modelo = LinearSVC()
modelo.fit(treino_x, treino_y.values.ravel())

from sklearn.metrics import accuracy_score

modelo = LinearSVC()
modelo.fit(treino_x, treino_y.values.ravel())
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print("A acurácia foi %.2f%%" % acuracia)





