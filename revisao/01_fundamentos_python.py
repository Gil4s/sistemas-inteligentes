"""
MÓDULO 01: PYTHON DO ZERO ABSOLUTO PARA SISTEMAS INTELIGENTES
Docente: Prof. Dr. Pedro Thiago Valério de Souza
Aluno: Gil | UFERSA

Instruções:
- Execute este arquivo no VS Code pelo terminal: python revisao/01_fundamentos_python.py
- Ou execute bloco a bloco usando a extensão Python (Shift + Enter na linha selecionada).
"""

# ==============================================================================
# TÓPICO 1: VARIÁVEIS, TIPOS PRIMITIVOS E F-STRINGS
# ==============================================================================
# Em Python:
# - Não declaramos tipo (é tipagem dinâmica).
# - Indentação (4 espaços) define blocos de código (não usa chaves {}).
# - Tipos primitivos básicos: int (inteiro), float (decimal), str (texto), bool (True/False).
# - F-strings: print(f"Texto {variavel}") permite interpolar variáveis facilmente.
#   Formatadores úteis: {valor:.2f} arredonda para 2 casas decimais.

print("--- TÓPICO 1: EXEMPLO ---")
temperatura_ambiente = 25.4  # float
pressao_mbar = 1013          # int
nome_usina = "Usina CCPP 1"  # str
em_operacao = True           # bool

print(f"{nome_usina} | Temp: {temperatura_ambiente:.1f}°C | Pressão: {pressao_mbar} mbar | Ativa: {em_operacao}")


# ------------------------------------------------------------------------------
# EXERCÍCIO 1 (Contexto Projeto 1 - Usina):
# Crie uma variável 'temp_celsius' com o valor 28.5.
# Converta essa temperatura para Fahrenheit usando a fórmula: F = (C * 9/5) + 32.
# Em seguida, exiba no terminal a mensagem:
# "Temperatura: 28.50°C equivale a XX.XX°F" (com 2 casas decimais).
# ------------------------------------------------------------------------------
# SEU CÓDIGO DO EXERCÍCIO 1 AQUI:




# ==============================================================================
# TÓPICO 2: ESTRUTURAS DE DADOS — LISTAS E DICIONÁRIOS
# ==============================================================================
# - LISTAS []: Sequência ordenada e mutável de itens.
#   exemplo = [10, 20, 30]
#   exemplo[0]      -> primeiro elemento (índice começa em 0)
#   exemplo[-1]     -> último elemento
#   exemplo.append(40) -> adiciona elemento no final
#   len(exemplo)    -> tamanho da lista
#   sum(exemplo)    -> soma de todos os números
#   min() e max()   -> menor e maior valor

# - DICIONÁRIOS {}: Coleções de pares chave-valor. É exatamente a estrutura de
#   uma linha de uma tabela ou dataset.
#   paciente = {"idade": 54, "sexo": 1, "colesterol": 240.0}
#   paciente["idade"] -> acessa o valor 54
#   paciente["doente"] = True -> adiciona uma nova chave

print("\n--- TÓPICO 2: EXEMPLO ---")
leituras_sensor = [22.4, 25.1, 24.8, 23.9]
print(f"Quantidade de leituras: {len(leituras_sensor)}")
print(f"Menor leitura: {min(leituras_sensor)} | Maior: {max(leituras_sensor)}")

# ------------------------------------------------------------------------------
# EXERCÍCIO 2 (Contexto Projeto 2 - Doenças Cardíacas):
# Crie um dicionário chamado 'paciente' contendo as seguintes informações:
# - "idade": 63
# - "sexo": "M"
# - "pressao": 145
# - "historico_pressao": uma lista com as últimas 3 medições: [140, 150, 145]
#
# Depois:
# 1. Calcule a média das medições de pressão do paciente usando sum() e len().
# 2. Adicione ao dicionário a chave "pressao_media" com esse valor calculado.
# 3. Imprima: "Paciente de XX anos teve pressão arterial média de YY.YY mmHg".
# ------------------------------------------------------------------------------
# SEU CÓDIGO DO EXERCÍCIO 2 AQUI:




# ==============================================================================
# TÓPICO 3: CONDICIONAIS (IF, ELIF, ELSE)
# ==============================================================================
# Sintaxe:
# if condicao:
#     # bloco indentado
# elif outra_condicao:
#     # bloco indentado
# else:
#     # bloco indentado
#
# Operadores de comparação: ==, !=, >, <, >=, <=
# Operadores lógicos: and, or, not

# ------------------------------------------------------------------------------
# EXERCÍCIO 3 (Contexto Projeto 3 - Vinhos):
# No dataset de vinhos, a nota de qualidade varia de 0 a 10.
# O problema 3 pede para agrupar em 3 categorias:
# - Se nota <= 5: "ruim"
# - Se nota for 6 ou 7: "médio"
# - Se nota >= 8: "bom"
#
# Crie uma variável 'nota_vinho = 7'.
# Escreva uma estrutura if/elif/else que defina a variável 'categoria'
# conforme a regra acima e imprima: "Vinho com nota X é classificado como: Y".
# ------------------------------------------------------------------------------
# SEU CÓDIGO DO EXERCÍCIO 3 AQUI:




# ==============================================================================
# TÓPICO 4: LAÇOS DE REPETIÇÃO (FOR) E LIST COMPREHENSIONS
# ==============================================================================
# Percorrer uma lista:
# for item in lista:
#     print(item)
#
# List Comprehension (Jeito pythônico e elegante de transformar listas):
# dobro = [x * 2 for x in lista]

# ------------------------------------------------------------------------------
# EXERCÍCIO 4 (Contexto Projeto 1 - Erro das Predições):
# Suponha que você tem os valores reais de produção de energia e os valores
# preditos pelo modelo:
# y_reais = [450.0, 460.0, 440.0, 470.0]
# y_pred =  [452.0, 458.0, 445.0, 468.0]
#
# 1. Usando um laço 'for' (ou list comprehension), calcule a lista de erros
#    absolutos entre cada valor real e seu respectivo predito.
#    Dica: para percorrer duas listas juntas, use: zip(y_reais, y_pred)
#    Dica 2: abs(a - b) retorna o valor absoluto (sem sinal negativo).
# 2. Calcule o Erro Médio Absoluto (MAE) somando os erros e dividindo pelo tamanho.
# 3. Imprima: "O Erro Médio Absoluto (MAE) foi de: X.XX MW".
# ------------------------------------------------------------------------------
# SEU CÓDIGO DO EXERCÍCIO 4 AQUI:




# ==============================================================================
# TÓPICO 5: FUNÇÕES (DEF)
# ==============================================================================
# Sintaxe:
# def nome_da_funcao(parametro1, parametro2):
#     resultado = parametro1 + parametro2
#     return resultado

# ------------------------------------------------------------------------------
# EXERCÍCIO 5 (Juntando Tudo):
# Transforme o cálculo do MAE do Exercício 4 em uma função reutilizável chamada:
# 'calcular_mae(reais, preditos)'
# A função deve retornar o valor do MAE calculado.
# Teste sua função com:
# teste_reais = [100.0, 200.0, 300.0]
# teste_pred  = [105.0, 195.0, 310.0]
# resultado = calcular_mae(teste_reais, teste_pred)
# Imprima o resultado na tela.
# ------------------------------------------------------------------------------
# SEU CÓDIGO DO EXERCÍCIO 5 AQUI:

