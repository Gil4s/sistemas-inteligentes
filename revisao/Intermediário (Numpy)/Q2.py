import numpy as np

## 1 -> Criar um array a partir de um alista:

sensores = np.array([25.4, 28.1,19.8, 32.0, 22.5])

## broadcasting (Operação em lote sem for):
## Multiplica todos por 2 e soma 10 simultaneamente em C:

ajustados = (sensores * 2) + 10

erros = np.array ([0.5, 0.2, 0.8, 0.1, 0.4])
sensores_corrigidos = sensores - erros

media = np.mean (sensores) ## Aqui eu estou fazendo a aritimética
desvio = np.std (sensores) ## Aqui eu estou fazendo o desvio padrão
minimo = np.min (sensores) ## Aqui eu estou fazendo o menor valor
maximo = np.max(sensores) ## Aqui eu estou fazendo o maior valor 
total = np.sum (sensores) ## Aqui eu estou fazendo a soma total

## validação por meio de uma questão 

## Não preciso importar o numpy, justamente pelo fato de eu ja ter importado
## A ideia é fazer uma lista de projetos por meio de uma usina usand oa variável AT (Ambient Temperature)

temperatura_celsius = np.array ([25.4, 28.1, 19.8, 32.0, 22.5, 27.3, 30.5])

temperatura_fahrenheit  = (temperatura_celsius * 9/5) + 32

media_fahrenheit = np.sum (temperatura_fahrenheit)
desvio_fahrenheit = np.std (temperatura_fahrenheit)
minima_fahrenheit = np.min (temperatura_fahrenheit)
maxima_fahrenheit = np.max (temperatura_fahrenheit)

print (f'Dados em Fahrenheit\nMedia: {media_fahrenheit:.2f}\nDesvio Padrão: {desvio_fahrenheit:.2f}\nTemperatura Mínima: {minima_fahrenheit}\nTemperatura Máxima: {maxima_fahrenheit}')