## REVISÃO PARTE 1

## As listas em python, como qualquer outra linguagem, elas são denominadas como colchetes, então podemos só entregar uma variável e dizer que ela é uma lista basicamente com colchetes

## pressões = [140, 150, 145]

## Funções nativas essenciais para listas numéricas:

pressões = [140, 150, 145]

total = sum(pressões)
## aqui é basicamente igual ao SUM que usamos em SQL, estamos aplicando uma soma de todas as componentes de um vetor, como temos 3 componentes, somanmos as 3 componentes basicamente 

quantidade = len (pressões) ## Quando eu uso o len, eu retorno quantos itens eu tenho na lista

media = total / quantidade 
## Por fim, o que fazemos é uma média, pegamos a variável que recebe o valor da soma e dividimos pela variável que recebe o valor referente a quantidade de termos na minha lista

print (f"A média é {media:.2f}")



## REVISÃO PARTE 2

## criando um DICIONÁRIO 

## eles guardam dados no formato de chave: valor (muito parecido com objetivos do JavaScript)

# Criando um dicionário com diferentes tipos de dados dentro dele
paciente = {
    "idade": 63,
    "sexo": "M",
    "fumante": True
}

## Veja que o dicionário funciona tipo uma struct, então com ele, podemos trabalhar os fundamentos de struct que temos em C

print (paciente["idade"]) ## Veja que idade não é uma variável convencional, eu tenho que colocar ela em ""
## usar os ":" depois de "idade" faz com que armazene o valor
## "idade": 63 -> como eu to colocando aspas, eu to basicamente usando um termo que fica dentro de paciente
## Se eu uso idade sem as aspas, eu basicamente estou usando uma palavra como se fosse uma variável que já existe no código, ou seja, não ia funcionar pois nesse caso, isso é uma característica de paciênte


## QUESTÃO 2

## No projeto 2, da lista de sistemas inteligentes, vamos trabalhar um modelo para prever doenças cardíacas com base em exames clínicos.
## Nessa questão de exercício, vamos desenvolver um dicionário para trabalhar a questão dos dados de um paciênte 

pacienteNovo = {
    "idade": 63, ## Estou dizendo que "idade" recebe um valor inteiro e é uma componente da minha struct
    "sexo": "M", ## Estou dizendo que a componente de sexo é uma string e armazena m
    "historico_pressao": [140, 150, 145],
    "pressaoMedia": 0 ## estou dizendo que a componente é uma lista e armazena 3 valores inteiros
    }

## Agora eu preciso calcular a média da pressão dessa paciente

total_pressao = sum(pacienteNovo[("historico_pressao")]) ## para acessar valores da struct em python, usamos os colchetes
## Veja que a operação vai acessar valores
## Dito isso, eu preciso ter como acessar, então eu dou prioridade a operação e depois acesso
pacienteNovo["pressaoMedia"] = total_pressao/len(pacienteNovo["historico_pressao"])

print (f"A pressão é {pacienteNovo["pressaoMedia"]:.2f}") ## Veja como é a sintaxe da formatação em float
## perceba que, quando eu escrevo o :.2f, eu preciso falar isso em cima do valor, e não atrelar isso na hora que estou acesando
## por isso que, quando vamos fazer dessa forma, precimaos configurar para que só depois de acessar o valor, coloquemos a formatação

