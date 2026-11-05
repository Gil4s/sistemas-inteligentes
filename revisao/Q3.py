## Relembrando condicionais 


## sintaxe

temperatura = 38

if temperatura > 37.5:
    print ("Estado Febril")
elif temperatura >= 36.0 and temperatura <= 37.5:
    print ("Temperatura normal")
else:
    print ("Hipotermia")


## Escrever temperatura >= 36.0 and temperatura <= 37.5 é a mesma coisa que escrever:
## 36.0 <= temperatura <= 37.5.

nota_vinho = 3
categoria = str()

if nota_vinho <= 5:
    categoria = "Vinho de qualidade ruim"
    print (categoria)
elif 5 < nota_vinho <= 7:
    categoria = "Vinho de qualidade Mediana"
    print (categoria)
else:
    print ("Vinho Exelente") 