# Problema 3 - Classificação de Qualidade de Vinhos com k-NN

## 1. Preparação dos Dados e Justificativa da Normalização

O dataset `winequality-red.csv` (1.599 amostras iniciais e 11 atributos físico-químicos) apresentou `240` linhas duplicadas exatas, que foram removidas para evitar vazamento entre treino, validação e teste — restando **1.359 amostras**. A variável `quality` foi recodificada em três categorias:
- `ruim` (notas `<= 5`): `640` amostras (`47,1%`)
- `medio` (notas `6` e `7`): `702` amostras (`51,7%`)
- `bom` (notas `>= 8`): `17` amostras (`1,3%`)

**Por que a normalização é obrigatória para o k-NN?**
O k-NN classifica cada amostra calculando a distância geométrica (distância euclidiana) até os vizinhos mais próximos. Como os atributos químicos têm escalas muito diferentes (por exemplo, `total sulfur dioxide` passa de 200, enquanto `density` e `chlorides` variam em casas decimais), sem a padronização (`StandardScaler`) os atributos de valores maiores dominariam o cálculo da distância e anulariam a influência das variáveis menores.

---

## 2. Divisão Treino e Teste Estratificada

Os dados foram divididos em 80% para treino (1.087 amostras) e 20% para teste (272 amostras) usando `stratify=y`. Com isso, a proporção das três classes (especialmente a classe `bom`, que representa apenas cerca de 1,3% do dataset) foi mantida igual nos dois conjuntos.

---

## 3. Treinamento e Escolha do k (Validação Cruzada de 5 Folds)

Foram testados os valores de `k` em `[1, 3, 5, 7, 9, 11, 13, 15]` com validação cruzada de 5 folds no conjunto de treino, usando `StandardScaler` dentro de um `Pipeline` para ajustar a escala separadamente em cada fold:
- `k = 1`: `0.6201`
- `k = 3`: `0.6486`
- `k = 5`: `0.6679`
- `k = 7`: `0.6652`
- `k = 9`: `0.6873`
- `k = 11`: `0.6974`
- `k = 13`: `0.7057`
- `k = 15`: `0.7010`

O valor escolhido pela maior acurácia média foi **`k = 13`** (`0.7057`), seguido por `k = 15` (`0.7010`) e `k = 11` (`0.6974`).

**Comportamento para valores muito baixos e muito altos de k:**
- **k muito baixo (ex: `k = 1`):** O modelo decide olhando apenas para o vizinho mais próximo, criando uma fronteira de decisão muito recortada e sensível a ruídos ou outliers (*overfitting*). Sem linhas duplicadas, `k = 1` teve a pior acurácia média da validação cruzada (`0.6201`).
- **k muito alto:** O modelo considera vizinhos muito distantes, suavizando demais a fronteira entre as classes (*underfitting*). Além disso, como a votação passa a envolver muitos vizinhos, as classes majoritárias (`medio` e `ruim`) sempre vencem a votação e apagam a classe minoritária (`bom`).

---

## 4. Avaliação do Modelo no Conjunto de Teste

Com `k = 13` avaliado no conjunto de teste (272 amostras), a **acurácia geral foi de `0.7537` (75,37%)**:

| Classe | Precisão | Recall | F1-score | Amostras no Teste |
| --- | --- | --- | --- | --- |
| `ruim` | 0.77 | 0.71 | 0.74 | 128 |
| `medio` | 0.74 | 0.81 | 0.77 | 141 |
| `bom` | 0.00 | 0.00 | 0.00 | 3 |

**Entre quais classes o modelo erra com mais frequência?**
- **Em quantidade absoluta de erros:** O modelo confunde mais entre as classes **`ruim` e `medio`** (37 vinhos ruins previstos como médios e 27 médios previstos como ruins), pois a maioria das amostras do dataset tem nota 5 (ruim) ou nota 6 (médio), que possuem propriedades químicas muito próximas.
- **Em termos proporcionais:** A classe **`bom`** sofre o maior erro relativo (todos os 3 vinhos bons do teste foram classificados como `medio`), devido ao forte desbalanceamento do conjunto, que possui apenas 17 vinhos bons no total (14 no treino e 3 no teste).
