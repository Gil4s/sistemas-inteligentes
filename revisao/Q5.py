## Vamos revisar "DEF"
## Vamos revisar "IDENTAÇÃO"
## Vamos revisar "RETORNO"


## veja que, se eu não identar (dar o tab na função que eu to definindo, eu vou ter um problema)

## no python, para definir uma fução se faz necessário a identação correta para aquilo que está dentro dela
def converter_celsius_para_fahrenheit(temp_celsius):
    temp_f = (temp_celsius * 9/5)+ 32
    return temp_f 

# Chamando a função

resultado = converter_celsius_para_fahrenheit (28.5)
print (f"Resultado: {resultado:.2f}º F")


## QUESTÃO 5

dados_reais = [100.0, 200.0, 300.0, 400.0]
dados_previstos = [105.0, 195.0, 310.0, 390.0]

def calcular_mae( reais, previstos ):
    calculo = [abs(r - p) for r,p in zip (reais, previstos)]
    ## MAE = Mean Absolute Error -> Erro médio absoluto
    return calculo;

print (calcular_mae(dados_reais,dados_previstos))
