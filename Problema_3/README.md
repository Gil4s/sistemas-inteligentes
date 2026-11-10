# Problema 3 - Classificação de Qualidade de Vinhos com k-NN

## 1. Preparação dos Dados e Justificativa da Normalização

O dataset `winequality-red.csv` (1.599 amostras e 11 atributos físico-químicos) teve a variável `quality` recodificada em três categorias:
- `ruim` (notas `<= 5`): `744` amostras (`46,5%`)
- `medio` (notas `6` e `7`): `837` amostras (`52,3%`)
- `bom` (notas `>= 8`): `18` amostras (`1,1%`)

**Por que a normalização é obrigatória para o k-NN?**
O k-NN classifica cada amostra calculando a distância geométrica (distância euclidiana) até os vizinhos mais próximos. Como os atributos químicos têm escalas muito diferentes (por exemplo, `total sulfur dioxide` passa de 200, enquanto `density` e `chlorides` variam em casas decimais), sem a padronização (`StandardScaler`) os atributos de valores maiores dominariam o cálculo da distância e anulariam a influência das variáveis menores.

---

## 2. Divisão Treino e Teste Estratificada

Os dados foram divididos em 80% para treino (1.279 amostras) e 20% para teste (320 amostras) usando `stratify=y`. Com isso, a proporção das três classes (especialmente a classe `bom`, que representa apenas cerca de 1,1% do dataset) foi mantida igual nos dois conjuntos.

---

## 3. Treinamento e Escolha do k (Validação Cruzada de 5 Folds)

Foram testados os valores de `k` em `[1, 3, 5, 7, 9, 11, 13, 15]` com validação cruzada de 5 folds no conjunto de treino:
- `k = 1`: `0.7209`
- `k = 3`: `0.6685`
- `k = 5`: `0.6794`
- `k = 7`: `0.6974`
- `k = 9`: `0.6998`
- `k = 11`: `0.7123`
- `k = 13`: `0.7154`
- `k = 15`: `0.7045`

O valor escolhido pela maior acurácia média foi **`k = 1`** (seguido por `k = 13` e `k = 11`).

**Comportamento para valores muito baixos e muito altos de k:**
- **k muito baixo (ex: `k = 1`):** O modelo decide olhando apenas para o vizinho mais próximo, criando uma fronteira de decisão muito recortada e sensível a ruídos ou outliers (*overfitting*). Neste dataset, `k = 1` teve bom resultado porque há amostras muito semelhantes de mesmos lotes.
- **k muito alto:** O modelo considera vizinhos muito distantes, suavizando demais a fronteira entre as classes (*underfitting*). Além disso, como a votação passa a envolver muitos vizinhos, as classes majoritárias (`medio` e `ruim`) sempre vencem a votação e apagam a classe minoritária (`bom`).

---

## 4. Avaliação do Modelo no Conjunto de Teste

Com `k = 1` avaliado no conjunto de teste (320 amostras), a **acurácia geral foi de `0.7656` (76,56%)**:

| Classe | Precisão | Recall | F1-score | Amostras no Teste |
| --- | --- | --- | --- | --- |
| `ruim` | 0.77 | 0.75 | 0.76 | 149 |
| `medio` | 0.76 | 0.80 | 0.78 | 167 |
| `bom` | 0.00 | 0.00 | 0.00 | 4 |

**Entre quais classes o modelo erra com mais frequência?**
- **Em quantidade absoluta de erros:** O modelo confunde mais entre as classes **`ruim` e `medio`**, pois a maioria das amostras do dataset tem nota 5 (ruim) ou nota 6 (médio), que possuem propriedades químicas muito próximas.
- **Em termos proporcionais:** A classe **`bom`** sofre o maior erro relativo (sendo classificada como `medio`), devido ao forte desbalanceamento do conjunto, que possui apenas 18 vinhos bons no total (14 no treino e 4 no teste).
