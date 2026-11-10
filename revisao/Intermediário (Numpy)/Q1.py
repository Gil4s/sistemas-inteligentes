## Voltando para a revisão de condicionais em python

## Operadores lógicos

## == (igualdade)
## != (diferente)
## > maior que
## < menor que
## >= maior igual que
## <= menor igual que
## and: igual em JAVA, todas as condições precisam assumir o estado de "Verdadeiro" (true)
## or : também como JAVA, basta que qualquer uma das condições sejam "Verdadeiras"
## not: negação lógica de digitais é uma boa forma de interpretar o not (passe se for um A "Barrado por exemplo")


## Praticando os operadores

idade = 65 
colesterol = 250 ## Estou ao mesmo tempo, configurando ao mesmo tempo o valor e tipando a variável
## a parte boa do python é justamente essa, podemos ao mesmo tempo que estamos valorando uma variável, podemos já deixar ela tipada também

## Exemplo usando a condição AND

if idade >= 60 and colesterol > 200:
    print("Grupo de risco cardiovascular")

tipo_dor = "angina_tipica"


## "in" e o "not in" a gente usa para checar por exemplo se um valor pertence ou não a uma lista
## a ideia é podermos validar por exemplo, se temos ou não uma componente que pertence a lista 

if tipo_dor in ["angina_tipica", "angina_atipica"]: ## sempre precisa lembrar de usar os 2 pontos aqui
    print("Sintoma relacionado a esforço físico")

## valor_se_verdadeiro if condicao else valor_se_falso 

## score = 75
## status = "Aprovado" if score >= 700 else "Em Análise"

## SOLICITAÇÃO PARA O USUÁRIO, PEDINDO O SALDO NA CONTA
saldo_conta = float(input("Qual o saldo da sua conta? ")) ## já defino como float por colocar o ponto

## CONFIGURANDO O HISTÓRICO DE CRÉDITO, PARA HERDAR CONFIGURAÇÕES
historico_credito = str(input("Qual o histórico de crédito que o serasa definiu para você? \n 1 - BOM \n 2 - RUIM \n 3 - CRÍTICO: "))

if historico_credito == "1":
    historico_credito = "BOM"
    duracao_meses = 12
    garantia = True
    juros = "3 por cento ao mês"

elif historico_credito == "2":
    historico_credito = "RUIM"
    duracao_meses = 24
    garantia = True
    juros = "5 por cento ao mês"

elif historico_credito == "3":
    historico_credito = "CRÍTICO"
    duracao_meses = 36
    garantia = False
    juros = "9 por cento ao mês"

else: 
    print("Opção inválida, definindo valores padrão de risco")
    historico_credito = "CRÍTICO"
    duracao_meses = 36
    garantia = False
    juros = "9 por cento ao mês"


## CONDICIONAL PARA A DEFINIÇÃO DE RISCO
if (saldo_conta >= 2000.0 or historico_credito == "BOM") and duracao_meses <= 36:
    nivel_de_risco = "BAIXO"
    
elif (saldo_conta > 0 and duracao_meses <= 12) or garantia == True:
    nivel_de_risco = "MODERADO"

else: ## Veja que, mesmo no meu else, eu preciso do uso da sintaxe dos dois pontos
    nivel_de_risco = "ALTO"


## Aqui eu estou dizendo o seguinte: o empréstimo só é aprovado se o nível de risco for diferente de ALTO
decisao = "Empréstimo Aprovado" if nivel_de_risco != "ALTO" else "Empréstimo Recusado"

print(f"\n--- ANÁLISE DE CRÉDITO --- \nHistórico: {historico_credito} | Saldo: R$ {saldo_conta:.2f} | Prazo: {duracao_meses} meses | Juros: {juros} \nNível de Risco: {nivel_de_risco} | Resultado: {decisao}")
