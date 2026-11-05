## Relembrando regressão linear


## o for em python é um foreach

valores = [10, 20, 30]

for v in valores:
    print (v)

## nessa estrutura, eu basicamente vou printando conforme eu vou tendo valores na minha lista
## no python, eu nem preciso definir o "i" tão usado nas outras linguagens
## eu posso basicamente printar a lista uma por uma para enquanto a lista tem valor
## logo, se eu tenho um valor, eu printo
## se eu não tenho um valor eu não printo


reais = [100, 200, 300]
preditos = [105, 195, 302, 30]

for r, p in zip (reais, preditos):
    print (f"real: {r} | Predito: {p}")

## Nesse caso, eu estou imprimindo para quando eu tenho reais e preditos valores existentes concomitantemente
## Veja que r e p herdam esses valores, mas a condição é dupla, pois o zip() junta as duas elemento a elemento
## se eu imprimir, a minha saída vai ser só para quando os 2 possuem valores de fato


## Agora a função ABS

absoluto = abs (100 - 105) ## essa função me entrega o valor absoluto de alguma coisa, eliminando o negativo
print (absoluto)

## agora vamos criar um list Comprehesion

erros = [abs(r - p) for r, p in zip (reais, preditos)]
## Nesse caso, eu estou pegando o valor absoluto referente a operação de r - p (onde ambos são listas) e cada um deles vao ser subtraido) 
## Eu estou guardando isso em uma lista
## veja que eu começo com colchetes, então o valro armazenado vai me retornar uma lista

print (erros)


## Questão 4

y_reais = [450.0, 460.0, 440.0, 470.0]
y_pred = [452.0, 458.0, 445.0, 468.0]


## objetivo, criar uma lista de erros abosolutos, a fim de mostrar os erros calculados referente aos resultados de minha previsão e os valores reais

## vamos começar criando a lista de erros resultantes
erros_resultantes = [abs (k - l) for k, l in zip (y_reais, y_pred)]
print (erros_resultantes)
