## Em python, quando trabalhandos com valores direto imputados em variáveis, ele já armazena a configuração do tipo de variável

temperatura = 25.4 ## aqui, por exemplo, como adicionarmos um ponto flutuante, já temos algo do tipo float por padrão
pressao = 1013 ## nesse caso, como adicionamos algo inteiro, já temos algo de fato como inteiro aqui
sensor = "Sensor A" ## str (já armazena o valor como string, justamente pelo fa)
ativo = True ## Veja que temos um valor verdadeiro aqui

## F-Strings (A forma mordena de formatar texto): Colocamos um f antes das asps e variáveis dentro de {}
nome = "Guilherme"
nota = 9.8765
print (f"olá {nome}, sua nota foi {nota:.2f}")
## Veja que eu entrei com o print, para demonstrar o que foi escrito na tela
## Veja que eu também entrei com as variáveis sendo chamadas nas chaves 



## Questão 1 

## No 1º projeto de Sistemas inteligentes, os sensores já enxergam os graus em Célsius


## Vamos criar uma variável 

temp_celsius = 28.5

## Vou trocar para fahrenheit  

temp_fahrenheit = (temp_celsius * (9/5) + 32) 

print (f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f}")

